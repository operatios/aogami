from collections.abc import Iterable, Mapping
from dataclasses import asdict, dataclass, field
from types import TracebackType
from typing import Final, Self

from pydantic import SecretStr, TypeAdapter, ValidationError
from typing_extensions import TypeForm

from aogami.exceptions import (
    DownloadError,
    InputFileTooLarge,
    SchemaMismatch,
    get_api_error,
)
from aogami.methods import TelegramMethods
from aogami.response import get_type_adapter
from aogami.transport import FileTypes, HttpxTransport
from aogami.types import InputFile, TelegramObject


def extract_files(
    value: object, files: dict[str, FileTypes], limit_mb: int = 50
) -> None:

    if isinstance(value, InputFile):
        # TODO: photos have a separate limit
        file_size = len(value.content) / (1000**2)
        if file_size > limit_mb:
            raise InputFileTooLarge(
                message=f"File is too large ({file_size:.0f} MB > {limit_mb} MB)",
                input_file=value,
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


def get_timeout(params: dict[str, object]) -> float:
    timeout = params.get("timeout", 0.0)

    if isinstance(timeout, int | float):
        return timeout

    raise RuntimeError(f"Invalid timeout type: {type(timeout)}")


@dataclass(slots=True)
class RequestArgs:
    content: bytes | None = None
    data: dict[str, JsonScalar] | None = None
    files: dict[str, FileTypes] = field(default_factory=dict)
    headers: dict[str, str] | None = None
    extra_read_timeout: float | None = None


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

        # TODO: set larger limit if we're using a Local Bot API server
        extract_files(params.values(), req.files)

        if req.files:
            # When uploading files, request params are sent as form data
            req.data = build_form_data(params)
        else:
            # Send params as JSON body
            req.content = PARAM_ADAPTER.dump_json(params, exclude_none=True)
            req.headers = {"Content-Type": "application/json"}

        if name == "getUpdates":
            req.extra_read_timeout = get_timeout(params)

        http_resp = await self.transport.post(
            url=f"/bot{self.token.get_secret_value()}/{name}",
            **asdict(req),
        )

        adapter = get_type_adapter(returns)

        try:
            resp = adapter.validate_json(http_resp.content)
        except ValidationError as exc:
            raise SchemaMismatch(
                message="Telegram API response does not match the expected schema",
                status_code=http_resp.status_code,
                content=http_resp.content,
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
            raise RuntimeError(f"{type(self).__name__}'s transport is closed")

        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        await self.transport.aclose()
