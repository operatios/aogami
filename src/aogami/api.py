from functools import cache
from typing import Final, cast

from pydantic import SecretStr, TypeAdapter
from typing_extensions import TypeForm

from aogami.methods import TelegramMethods
from aogami.transport import HttpxTransport
from aogami.types import Response


@cache
def get_type_adapter[T](type_: TypeForm[T]) -> TypeAdapter[Response[T]]:
    return TypeAdapter(Response[type_])  # ty: ignore[invalid-type-form]


PARAM_ADAPTER: Final = TypeAdapter(object)


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

        content = PARAM_ADAPTER.dump_json(params)
        http_resp = await self.transport.request(
            f"/bot{self.token.get_secret_value()}/{name}",
            content,
        )

        # @cache erases the return type, so we have to manually set the type hint
        adapter: TypeAdapter[Response[T]] = get_type_adapter(returns)
        resp = adapter.validate_json(http_resp.content)

        # TODO: TelegramAPIError(error_code, description, parameters)
        if not resp.ok:
            raise ValueError(resp.description)

        return cast(T, resp.result)
