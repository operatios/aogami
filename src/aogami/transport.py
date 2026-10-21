from collections.abc import Mapping

from httpx2 import AsyncClient, HTTPError, Timeout
from httpx2 import Response as HttpxResponse
from httpx2._types import FileTypes, RequestContent, RequestData

from aogami.exceptions import NetworkError


def extend_read(timeout: Timeout, extra: int | None) -> Timeout:
    if timeout.read is None or extra is None:
        return timeout

    return Timeout(
        connect=timeout.connect,
        read=timeout.read + extra,
        write=timeout.write,
        pool=timeout.pool,
    )


class HttpxTransport:
    def __init__(self, base_url: str, proxy: str | None = None) -> None:
        # TODO: http2=True
        self.client = AsyncClient(base_url=base_url, proxy=proxy)

    async def aclose(self) -> None:
        await self.client.aclose()

    @property
    def is_closed(self) -> bool:
        return self.client.is_closed

    async def post(
        self,
        url: str,
        *,
        content: RequestContent | None = None,
        data: RequestData | None = None,
        files: Mapping[str, FileTypes] | None = None,
        headers: Mapping[str, str] | None = None,
        extra_read_timeout: int | None = None,
    ) -> HttpxResponse:

        timeout = extend_read(self.client.timeout, extra_read_timeout)

        try:
            return await self.client.post(
                url,
                content=content,
                data=data,
                files=files,
                headers=headers,
                timeout=timeout,
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
