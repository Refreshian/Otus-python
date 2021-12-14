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

async def fetch_json(session: ClientSession, url: str) -> dict:
    async with session.get(url) as responce:
        return await responce.json()

# async def fetch_field(service: Service) -> Optional[str]:
#     async with ClientSession() as session:
#         json_data = await fetch_json(session, service.url)
#         return json_data

async def fetch_users_data(service: USERS_DATA_URL) -> dict:
    async with ClientSession() as session:
        res = await fetch_json(session, service)
        return res

async def fetch_posts_data(service: POSTS_DATA_URL) -> dict:
    async with ClientSession() as session:
        res = await fetch_json(session, service)
        return res

async def run_main():
    res = await fetch_posts_data(POSTS_DATA_URL)
    log.info("Result users data for url %r %s", POSTS_DATA_URL, res)
    # for service in SERVICES:
    #     res = await fetch_field(service)
    #     log.info("Result for Service %r is %s", service.name, res)

def main():
    asyncio.run(run_main())

if __name__ == "__main__":
    main()