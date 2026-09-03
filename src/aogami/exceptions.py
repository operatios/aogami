from aogami.types import ResponseParameters


class TelegramError(Exception):
    def __init__(
        self,
        *,
        description: str,
        error_code: int,
        parameters: ResponseParameters | None = None,
    ) -> None:
        self.error_code = error_code
        self.description = description
        self.parameters = parameters

    def __str__(self) -> str:
        return f"[{self.error_code}] {self.description}"
