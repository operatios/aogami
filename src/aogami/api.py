from collections.abc import Iterable
from dataclasses import asdict, dataclass, field
from functools import cache
from types import TracebackType
from typing import Final, Self

from pydantic import SecretStr, TypeAdapter
from typing_extensions import TypeForm

from aogami.exceptions import TelegramError
from aogami.methods import TelegramMethods
from aogami.transport import FileTypes, HttpxTransport
from aogami.types import ResponseParameters, TelegramObject
from aogami.types_manual import InputFile

PARAM_ADAPTER: Final = TypeAdapter(object)


class Response[T](TelegramObject):
    ok: bool
    result: T | None = None
    error_code: int | None = None
    description: str | None = None
    parameters: ResponseParameters | None = None


@cache
def get_type_adapter[T](type_: TypeForm[T]) -> TypeAdapter[Response[T]]:
    # TODO: stop ignoring once this false positive is fixed upstream
    return TypeAdapter(Response[type_])  # ty: ignore[invalid-type-form]


def extract_files(value: object, files: dict[str, FileTypes]) -> None:
    if isinstance(value, InputFile):
        if value.filename:
            files[value.id] = value.filename, value.content
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

        # TODO: see AsyncClient.build_request()
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

        # @cache erases the return type, so we have to manually set the type hint
        adapter: TypeAdapter[Response[T]] = get_type_adapter(returns)
        resp = adapter.validate_json(http_resp.content)

        # TODO: handle 429
        if not resp.ok:
            raise TelegramError(resp.error_code, resp.description, resp.parameters)

        assert resp.result is not None

        return resp.result

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        await self.transport.aclose()
