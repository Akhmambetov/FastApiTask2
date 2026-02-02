import asyncio
import datetime
import json
import random
import uuid
from typing import Iterable

from starlette.requests import Request

from src.core.config import RETRY_TIMEOUT, STREAM_DELAY
from src.utils.random_words import get_random_word


def get_new_messages() -> Iterable:
    return [
        {
            "event": "new_message",
            "retry": RETRY_TIMEOUT,
            "data": json.dumps(
                {
                    "word": get_random_word(),
                    "number": random.randint(0, 1000),
                    "datetime": datetime.datetime.now().isoformat(
                        sep="T", timespec="auto"
                    ),
                }
            ),
            "id": str(uuid.uuid4()),
        }
    ]

async def event_creator(request: Request):
    while True:
        if await request.is_disconnected():
            break
        for message in get_new_messages():
            yield message
        await asyncio.sleep(STREAM_DELAY)