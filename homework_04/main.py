"""
Домашнее задание №3
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""

import asyncio

from sqlalchemy.orm import session

from homework_04.models import User, Post, init_tables
from homework_04.models import Session
from jsonplaceholder_requests import fetch_users_data, fetch_posts_data, POSTS_DATA_URL, USERS_DATA_URL


async def user_data(users: list):

    async with Session() as session:
        async with session.begin():
            session.add_all(
                users
            )

async def post_data(posts: list):

    async with Session() as session:
        async with session.begin():
            session.add_all(
                posts
            )

async def create_users(users_data=None, posts_data=None):
    async with Session() as session:
        async with session.begin():
            for user in users_data:
                session.add(User(id=user['id'], name=user['name'], username=user['username'], email=user['email']))

            for post in posts_data:
                session.add(Post(id=post['id'], user_id=post['userId'], title=post['title'], body=post['body']))

async def async_main():

    await init_tables()
    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data(),
    )
    await create_users(users_data, posts_data)



def main():
    asyncio.run(async_main())

if __name__ == "__main__":
    main()
