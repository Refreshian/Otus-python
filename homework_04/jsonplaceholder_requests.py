"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"

import asyncio
import logging
from dataclasses import dataclass
from typing import Optional
from aiohttp import ClientSession

DEFAULT_FORMAT = "%(asctime)s %(levelname)-8s [%(name)-8s] (%(filename)s:%(funcName)s:%(lineno)d) %(message)s"
logging.basicConfig(format=DEFAULT_FORMAT, level=logging.DEBUG)
log = logging.getLogger(__name__)

# @dataclass
# class Service:
#     name: str
#     url: str
#     field: str
#
# SERVICES = [
#     Service('user', USERS_DATA_URL, "id"),
#     Service('post', POSTS_DATA_URL, "title")
# ]

async def fetch_json(url: str):
    async with ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def fetch_users_data() -> list:
    return await fetch_json(USERS_DATA_URL)


async def fetch_posts_data() -> list:
    return await fetch_json(POSTS_DATA_URL)

async def run_main():
    res = await fetch_posts_data()
    log.info("Result users data for url %r %s", POSTS_DATA_URL, res)


def main():
    asyncio.run(run_main())

if __name__ == "__main__":
    main()