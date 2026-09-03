from aogami.types import ResponseParameters


class TelegramError(Exception):
    def __init__(
        self,
        error_code: int | None,
        description: str | None,
        parameters: ResponseParameters | None,
    ) -> None:
        self.error_code = error_code
        self.description = description
        self.parameters = parameters

    def __str__(self) -> str:
        return (
            f"TelegramError<{self.error_code}>: {self.description} ({self.parameters})"
        )
