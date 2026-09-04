from collections.abc import Iterable
from dataclasses import asdict, dataclass, field
from functools import cache
from types import TracebackType
from typing import Annotated, Final, Literal, Self, cast

from pydantic import Field, SecretStr, TypeAdapter
from typing_extensions import TypeForm

from aogami.exceptions import TelegramError
from aogami.methods import TelegramMethods
from aogami.transport import FileTypes, HttpxTransport
from aogami.types import InputFile, ResponseParameters, TelegramObject

PARAM_ADAPTER: Final = TypeAdapter(object)


class ResponseOk[T](TelegramObject):
    ok: Literal[True] = Field(True, exclude=True)

    result: T
    description: str | None = None


class ResponseErr(TelegramObject):
    ok: Literal[False] = Field(False, exclude=True)

    error_code: int
    description: str
    parameters: ResponseParameters | None = None


type Response[T] = Annotated[ResponseOk[T] | ResponseErr, Field(discriminator="ok")]


@cache
def get_type_adapter[T](type_: TypeForm[T]) -> TypeAdapter[Response[T]]:
    # TODO: stop ignoring once this false positive is fixed upstream
    return TypeAdapter(Response[type_])  # ty: ignore[invalid-type-form]


def extract_files(value: object, files: dict[str, FileTypes]) -> None:
    if isinstance(value, InputFile):
        if value.filename:
            files[value.id] = value.filename, value.content, value.content_type
        else:
            files[value.id] = value.content

    elif isinstance(value, TelegramObject):
        for _, field_value in value:
            extract_files(field_value, files)

    elif isinstance(value, Iterable) and not isinstance(value, str | bytes):
        for i in value:
            extract_files(i, files)


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


@dataclass
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

        resp = adapter.validate_json(http_resp.content)

        # TODO: handle 429
        if not resp.ok:
            raise TelegramError(**resp.model_dump())

        return resp.result

    async def download(self, file_id: str) -> bytes:
        file = await self.get_file(file_id=file_id)
        assert file.file_path

        http_resp = await self.transport.get(
            f"/file/bot{self.token.get_secret_value()}/{file.file_path}"
        )
        http_resp.raise_for_status()

        return http_resp.content

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        await self.transport.aclose()
