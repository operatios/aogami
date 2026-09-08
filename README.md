# aogami

A type-safe Telegram Bot API framework for Python.

## Status

This project is still work in progress. The API surface may change without notice.

## Features

- Types and methods generated directly from the Telegram Bot API spec
- Every Telegram object modeled as a pydantic model, with full typing
- Async client built on top of httpx2
- Automatic detection and upload of files inside request parameters
- A typed exception for each Telegram/HTTP error code
- A `download` helper for downloading files

## Requirements

- Python 3.14 or newer

## Installation

Install it directly from the repository with uv:

```bash
uv add "aogami @ git+https://github.com/operatios/aogami"
```

## Basic usage

```python
import asyncio

from pydantic import SecretStr

from aogami.api import TelegramAPI


async def main() -> None:
    async with TelegramAPI(token=SecretStr("YOUR_BOT_TOKEN")) as api:
        me = await api.get_me()
        print(me.username)

        await api.send_message(chat_id=123456789, text="Hello from aogami")


asyncio.run(main())
```

Method names follow the Telegram API's naming, converted to snake_case: `sendMessage` becomes `send_message`, `getMe` becomes `get_me`, and so on.

## Sending files

```python
from aogami.types import InputFile

with open("photo.jpg", "rb") as f:
    photo = InputFile(content=f.read(), filename="photo.jpg")

await api.send_photo(chat_id=123456789, photo=photo)
```

## Sending a media group

```python
from aogami.types import InputFile, InputMediaPhoto

media = []

for filename in ("photo1.jpg", "photo2.jpg", "photo3.jpg"):
    with open(filename, "rb") as f:
        media.append(
            InputMediaPhoto(media=InputFile(content=f.read()))
        )

await api.send_media_group(chat_id=123456789, media=media)
```

## Downloading files

```python
data = await api.download(file_id="some_file_id")

with open("photo.jpg", "wb") as f:
    f.write(data)
```

## Error handling

```python
from aogami.exceptions import BadRequest, RetryAfter

try:
    await api.send_message(chat_id=123456789, text="Hello")
except RetryAfter as e:
    print(f"Rate limited, retry after {e.retry_after} seconds")
except BadRequest as e:
    print(e.description)
```

## How types and methods are generated

`tools/generate.py` downloads the Telegram Bot API spec from the [telegram-bot-api-spec](https://github.com/PaulSonOfLars/telegram-bot-api-spec) project and renders `types.py` and `methods.py` from the Mako templates in `tools/templates`.

To regenerate:

```bash
uv run tools/generate.py
```

Flags:
- `--refresh` re-downloads the spec instead of using the cached copy
- `--no-ruff` skips running ruff check and format on the generated files
