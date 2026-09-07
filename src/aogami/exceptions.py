from aogami.response import ResponseErr
from aogami.types import File, InputFile, ResponseParameters


class AogamiError(Exception): ...


class DownloadError(AogamiError):
    def __init__(self, message: str, file: File) -> None:
        self.file = file

        super().__init__(message)


class InputFileTooLarge(AogamiError):
    def __init__(self, message: str, input_file: InputFile) -> None:
        self.input_file = input_file

        super().__init__(message)


class NetworkError(AogamiError):
    def __init__(self, message: str, exc: Exception) -> None:
        self.exc = exc

        super().__init__(message)


class ValidationError(AogamiError):
    def __init__(
        self, message: str, status_code: int, content: bytes, exc: Exception
    ) -> None:
        self.status_code = status_code
        self.content = content
        self.exc = exc

        super().__init__(message)


class APIError(AogamiError):
    def __init__(
        self,
        description: str,
        error_code: int,
        parameters: ResponseParameters | None = None,
    ) -> None:
        self.error_code = error_code
        self.description = description
        self.parameters = parameters

        super().__init__(description)

    def __str__(self) -> str:
        return f"[{self.error_code}] {self.description}"


class BadRequest(APIError):
    """400: BadRequest"""


class MigrateToChat(APIError):
    """400: BadRequest"""

    @property
    def migrate_to_chat_id(self) -> int:
        assert self.parameters is not None
        assert self.parameters.migrate_to_chat_id is not None

        return self.parameters.migrate_to_chat_id


class Unauthorized(APIError):
    """401: Unauthorized"""


class Forbidden(APIError):
    """403: Forbidden"""


class Conflict(APIError):
    """409: Conflict"""


class EntityTooLarge(APIError):
    """413: Request Entity Too Large"""


class RetryAfter(APIError):
    """429: Too Many Requests"""

    @property
    def retry_after(self) -> int:
        assert self.parameters is not None
        assert self.parameters.retry_after is not None

        return self.parameters.retry_after


class ServerError(APIError):
    """error_code >= 500"""


def get_api_error(resp: ResponseErr) -> APIError:
    if resp.parameters is not None:
        if resp.parameters.migrate_to_chat_id is not None:
            return MigrateToChat(resp.description, resp.error_code, resp.parameters)
        if resp.parameters.retry_after is not None:
            return RetryAfter(resp.description, resp.error_code, resp.parameters)

    match resp.error_code:
        case 400:
            cls = BadRequest
        case 401:
            cls = Unauthorized
        case 403:
            cls = Forbidden
        case 409:
            cls = Conflict
        case 413:
            cls = EntityTooLarge
        case code if code >= 500:
            cls = ServerError
        case _:
            cls = APIError

    return cls(resp.description, resp.error_code, resp.parameters)
