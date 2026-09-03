from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field, model_serializer


class TelegramObject(BaseModel):
    model_config = ConfigDict(frozen=True)


class InputFile(TelegramObject):
    content: bytes
    filename: str | None = None
    content_type: str | None = None

    id: str = Field(default_factory=lambda: uuid4().hex)

    @model_serializer()
    def serialize(self) -> str:
        return f"attach://{self.id}"
