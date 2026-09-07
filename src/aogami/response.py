from functools import cache
from typing import Annotated, Literal

from pydantic import Field, TypeAdapter
from typing_extensions import TypeForm

from aogami.types import ResponseParameters, TelegramObject


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
