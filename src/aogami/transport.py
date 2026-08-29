from httpx2 import AsyncClient
from httpx2 import Response as HttpxResponse


class HttpxTransport:
    def __init__(self, base_url: str, proxy: str | None = None) -> None:
        # TODO: set timeout for getUpdates
        # TODO: close the client?
        self.client = AsyncClient(
            base_url=base_url,
            proxy=proxy,
        )

    async def request(self, url: str, content: bytes) -> HttpxResponse:
        return await self.client.post(
            url,
            content=content,
            headers={"Content-Type": "application/json"},
        )
