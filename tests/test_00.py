from collections.abc import AsyncGenerator

import pytest
from pydantic import AnyUrl, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

from aogami.methods import TelegramAPI


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    token: SecretStr
    proxy: AnyUrl


@pytest.fixture(scope="session")
def settings() -> Settings:
    return Settings()


@pytest.fixture
async def client(settings: Settings) -> AsyncGenerator[TelegramAPI]:
    yield TelegramAPI(
        settings.token.get_secret_value(),
        str(settings.proxy),
    )


@pytest.mark.anyio
async def test_get_me(client: TelegramAPI) -> None:
    await client.get_me()
