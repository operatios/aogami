from collections.abc import Mapping

from httpx2 import AsyncClient
from httpx2 import Response as HttpxResponse
from httpx2._types import FileTypes, RequestContent, RequestData


class HttpxTransport:
    def __init__(self, base_url: str, proxy: str | None = None) -> None:
        self.client = AsyncClient(
            base_url=base_url,
            proxy=proxy,
        )

    async def aclose(self) -> None:
        await self.client.aclose()

    async def post(
        self,
        url: str,
        *,
        content: RequestContent | None = None,
        data: RequestData | None = None,
        files: Mapping[str, FileTypes] | None = None,
        headers: Mapping[str, str] | None = None,
        timeout: float | None = None,
    ) -> HttpxResponse:

        return await self.client.post(
            url,
            content=content,
            data=data,
            files=files,
            headers=headers,
            timeout=timeout if timeout is not None else self.client.timeout,
        )

    async def get(self, url: str) -> HttpxResponse:
        return await self.client.get(url)
