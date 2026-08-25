from functools import cache
from typing import Final, cast

from pydantic import TypeAdapter
from typing_extensions import TypeForm

from aogami.transport import HttpxTransport
from aogami.types import Response


@cache
def get_type_adapter[T](type: TypeForm[T]) -> TypeAdapter[Response[T]]:
    return TypeAdapter(Response[type])  # ty: ignore[invalid-type-form]


PARAM_ADAPTER: Final = TypeAdapter(object)


class Base:
    def __init__(
        self,
        token: str,
        proxy: str | None = None,
    ) -> None:
        self.transport = HttpxTransport(
            base_url="https://api.telegram.org/",
            proxy=proxy,
        )
        self.token = token

    async def method[T](
        self, _method_name: str, _type: TypeForm[T], **params: object
    ) -> T:

        params = {k: v for k, v in params.items() if v is not None}

        content = PARAM_ADAPTER.dump_json(params)
        resp = await self.transport.request(
            f"/bot{self.token}/{_method_name}",
            content,
        )

        # @cache erases the return type, so we have to manually set the type hint
        adapter: TypeAdapter[Response[T]] = get_type_adapter(_type)
        data = adapter.validate_json(resp.content)

        if not data.ok:
            raise ValueError(data.description)

        return cast(T, data.result)
