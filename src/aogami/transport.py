from collections.abc import Mapping

from httpx2 import AsyncClient, HTTPError
from httpx2 import Response as HttpxResponse
from httpx2._types import FileTypes, RequestContent, RequestData

from aogami.exceptions import NetworkError


class HttpxTransport:
    def __init__(self, base_url: str, proxy: str | None = None) -> None:
        # TODO: http2=True
        self.client = AsyncClient(base_url=base_url, proxy=proxy)

    @property
    def is_closed(self) -> bool:
        return self.client.is_closed

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
        try:
            return await self.client.post(
                url,
                content=content,
                data=data,
                files=files,
                headers=headers,
                timeout=timeout if timeout is not None else self.client.timeout,
            )
        except HTTPError as exc:
            raise NetworkError(str(exc), exc) from exc

    async def download(self, url: str) -> bytes:
        try:
            resp = await self.client.get(url)
            resp.raise_for_status()
        except HTTPError as exc:
            raise NetworkError(str(exc), exc) from exc

        return resp.content
