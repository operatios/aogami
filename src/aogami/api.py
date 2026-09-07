from collections.abc import Iterable, Mapping
from dataclasses import asdict, dataclass, field
from types import TracebackType
from typing import Final, Self, cast

import pydantic
from pydantic import SecretStr, TypeAdapter
from typing_extensions import TypeForm

from aogami.exceptions import (
    DownloadError,
    InputFileTooLarge,
    ValidationError,
    get_api_error,
)
from aogami.methods import TelegramMethods
from aogami.response import Response, get_type_adapter
from aogami.transport import FileTypes, HttpxTransport
from aogami.types import InputFile, TelegramObject


def extract_files(
    value: object, files: dict[str, FileTypes], limit_mb: int = 50
) -> None:

    if isinstance(value, InputFile):
        # TODO: photos have a separate limit
        max_size = limit_mb * (1000**2)
        if len(value.content) > max_size:
            raise InputFileTooLarge(
                message=f"File is too big (>{limit_mb} MB)", input_file=value
            )

        if value.filename:
            files[value.id] = value.filename, value.content, value.content_type
        else:
            files[value.id] = value.content

    elif isinstance(value, TelegramObject):
        for _, field_value in value:
            extract_files(field_value, files, limit_mb)

    elif isinstance(value, Mapping):
        for v in value.values():
            extract_files(v, files, limit_mb)

    elif isinstance(value, Iterable) and not isinstance(value, str | bytes):
        for i in value:
            extract_files(i, files, limit_mb)


PARAM_ADAPTER: Final = TypeAdapter(object)
JsonScalar = str | int | float | bool | None


def build_form_data(params: dict[str, object]) -> dict[str, JsonScalar]:
    # Use `exclude_none` to exclude optional fields from TelegramObjects
    serialized_params = PARAM_ADAPTER.dump_python(
        params, mode="json", exclude_none=True
    )

    form_data: dict[str, JsonScalar] = {}

    for k, v in serialized_params.items():
        if isinstance(v, JsonScalar):
            form_data[k] = v
        else:
            form_data[k] = PARAM_ADAPTER.dump_json(v).decode()
    return form_data


def get_timeout_with_padding(
    params: dict[str, object], padding: float = 5.0
) -> float | None:
    timeout = params.get("timeout")
    if isinstance(timeout, int | float):
        return timeout + padding

    return None


@dataclass(slots=True)
class RequestArgs:
    content: bytes | None = None
    data: dict[str, JsonScalar] | None = None
    files: dict[str, FileTypes] = field(default_factory=dict)
    headers: dict[str, str] | None = None
    timeout: float | None = None


class TelegramAPI(TelegramMethods):
    def __init__(
        self,
        token: SecretStr,
        proxy: str | None = None,
    ) -> None:
        self.transport = HttpxTransport(
            base_url="https://api.telegram.org/",
            proxy=proxy,
        )
        self.token = token

    async def method[T](
        self, name: str, returns: TypeForm[T], /, **params: object
    ) -> T:

        params = {k: v for k, v in params.items() if v is not None}

        req = RequestArgs()
        # TODO: set larger limit if we're using a local Bot API server
        extract_files(params.values(), req.files)

        if req.files:
            req.data = build_form_data(params)
        else:
            req.content = PARAM_ADAPTER.dump_json(params, exclude_none=True)
            req.headers = {"Content-Type": "application/json"}

        if name == "getUpdates":
            req.timeout = get_timeout_with_padding(params)

        http_resp = await self.transport.post(
            url=f"/bot{self.token.get_secret_value()}/{name}",
            **asdict(req),
        )

        # TODO: remove cast if this false positive is fixed upstream
        # We have to cast here since @cache destroys the function signature
        adapter = cast(TypeAdapter[Response[T]], get_type_adapter(returns))

        try:
            resp = adapter.validate_json(http_resp.content)
        except pydantic.ValidationError as exc:
            raise ValidationError(
                message="Telegram API response does not match the expected schema",
                status_code=http_resp.status_code,
                content=http_resp.content,
                exc=exc,
            ) from exc

        if not resp.ok:
            raise get_api_error(resp)

        return resp.result

    async def download(self, file_id: str) -> bytes:
        file = await self.get_file(file_id=file_id)
        if not file.file_path:
            raise DownloadError("File path missing from file", file=file)

        return await self.transport.download(
            f"/file/bot{self.token.get_secret_value()}/{file.file_path}"
        )

    async def __aenter__(self) -> Self:
        if self.transport.is_closed:
            raise RuntimeError(f"{self.__class__.__name__}'s transport is closed")
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> bool | None:
        await self.transport.aclose()
