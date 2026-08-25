from httpx2 import AsyncClient, Response


class HttpxTransport:
    def __init__(self, base_url: str, proxy: str | None = None) -> None:
        self.client = AsyncClient(
            base_url=base_url,
            proxy=proxy,
        )

    async def request(self, url: str, content: bytes) -> Response:
        return await self.client.post(
            url,
            content=content,
            headers={"Content-Type": "application/json"},
        )
