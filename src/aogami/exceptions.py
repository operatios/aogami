from typing import Final

from aogami.response import ResponseErr
from aogami.types import File, InputFile, ResponseParameters


class AogamiError(Exception):
    pass


class DownloadError(AogamiError):
    def __init__(self, message: str, file: File) -> None:
        super().__init__(message)

        self.file = file


class InputFileTooLarge(AogamiError):
    def __init__(self, message: str, input_file: InputFile) -> None:
        super().__init__(message)

        self.input_file = input_file


class NetworkError(AogamiError):
    pass


class SchemaMismatch(AogamiError):
    def __init__(self, message: str, status_code: int, content: bytes) -> None:
        super().__init__(message)

        self.status_code = status_code
        self.content = content


class APIError(AogamiError):
    def __init__(
        self,
        description: str,
        error_code: int,
        parameters: ResponseParameters | None = None,
    ) -> None:
        super().__init__(f"[{error_code}] {description}")

        self.description = description
        self.error_code = error_code
        self.parameters = parameters


class BadRequest(APIError):
    """400"""


class MigrateToChat(BadRequest):
    def __init__(
        self, description: str, error_code: int, parameters: ResponseParameters
    ) -> None:
        super().__init__(description, error_code, parameters)

        assert parameters.migrate_to_chat_id is not None
        self.migrate_to_chat_id = parameters.migrate_to_chat_id


class Unauthorized(APIError):
    """401"""


class Forbidden(APIError):
    """403"""


class Conflict(APIError):
    """409"""


class EntityTooLarge(APIError):
    """413"""


class RetryAfter(APIError):
    """429"""

    def __init__(
        self, description: str, error_code: int, parameters: ResponseParameters
    ) -> None:
        super().__init__(description, error_code, parameters)

        assert parameters.retry_after is not None
        self.retry_after: int = parameters.retry_after


class ServerError(APIError):
    """5xx"""


_ERRORS_BY_CODE: Final[dict[int, type[APIError]]] = {
    400: BadRequest,
    401: Unauthorized,
    403: Forbidden,
    409: Conflict,
    413: EntityTooLarge,
}


def get_api_error(resp: ResponseErr) -> APIError:

    if resp.parameters is not None:
        if resp.parameters.migrate_to_chat_id is not None:
            return MigrateToChat(resp.description, resp.error_code, resp.parameters)
        if resp.parameters.retry_after is not None:
            return RetryAfter(resp.description, resp.error_code, resp.parameters)

    cls = _ERRORS_BY_CODE.get(resp.error_code)
    if cls is None:
        cls = ServerError if resp.error_code >= 500 else APIError

    return cls(resp.description, resp.error_code, resp.parameters)
