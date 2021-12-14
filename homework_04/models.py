"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""
import asyncio
import os

from sqlalchemy import select, Integer, ForeignKey, Text
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import joinedload, selectinload, sessionmaker
from sqlalchemy.orm import declared_attr, InstrumentedAttribute
from sqlalchemy.ext.declarative import declarative_base

# from blog_app.models import Base, User, Post, Tag


engine = create_async_engine(
    "postgresql+asyncpg://user:password@localhost/blog_app",
    echo=True,
)


PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"

Base = declarative_base()
Session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)

from sqlalchemy import (
    Column,
    String,
    Boolean,
)
from sqlalchemy.orm import relationship
from base import Base
# from .mixins import TimestampMixin


class User(Base):

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(32), unique=True)
    username = Column(String(32), unique=True)
    email = Column(String(32), unique=True)

    posts = relationship("Post", back_populates="user")

    def __str__(self):
        return f"{self.__class__.__name__}(name={self.name}, " \
               f"username={self.username!r}, email={self.email})"


class Post(Base):
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    title = Column(Text, nullable=False, default="", server_default="")
    body = Column(Text, nullable=False, default="", server_default="")

    user = relationship("User", back_populates="posts")

