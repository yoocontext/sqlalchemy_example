from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import BigInteger, ForeignKey

from app.infra.models.base import BaseORM
from app.infra.models.mixins import IntPKMixin, TimeMixin


"""
тут я показываю связь один ко многим где один это User, а многие это Post. 
типа у одного юзера может быть много постов, но у поста может быть только один User
"""


class UserORM(
    BaseORM, IntPKMixin, TimeMixin
):  # наследуюсь от миксинов чтобы не писать одно и тоже
    __tablename__ = "users"

    telegram_id: Mapped[int] = mapped_column(
        BigInteger
    )  # тут BigInteger так как у телеграмма большие id на 11 символов
    first_name: Mapped[str]
    second_name: Mapped[str]

    posts: Mapped[list["PostORM"]] = relationship(back_populates="user")


class PostORM(BaseORM, IntPKMixin, TimeMixin):
    __tablename__ = "posts"

    title: Mapped[str]
    text: Mapped[str]
    enable: Mapped[bool]

    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id"))

    user: Mapped["UserORM"] = relationship(back_populates="posts")


# p.s лень объяснять подробно чо тут как работает могу в войсе потом
