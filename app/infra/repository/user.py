from dishka import Scope
from sqlalchemy import Result, Select, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.infra.models.user import UserORM, PostORM
from app.infra.repository.base import BaseRepositoryORM


class UserRepositoryORM(BaseRepositoryORM):
    async def get_by_id(self, required_id: int) -> UserORM | None:
        """получаю модель декларативно типа высокоуровнего просто говорю чо сделать а не как"""

        user: UserORM | None = await self.session.get(UserORM, required_id)
        return user

    async def get_by_id_imperative(self, required_id: int) -> UserORM | None:
        """получаю модель императивно типа пишу прям ручками конкретную реализацию"""

        stmt: Select[tuple[UserORM]] = select(UserORM).where(UserORM.id == required_id)
        result: Result = await self.session.execute(stmt)
        user: UserORM | None = result.scalars().one_or_none()
        return user

    async def add_user(self, user: UserORM) -> UserORM:
        self.session.add(user)
        return user

    async def add_post(self, user: UserORM, post: PostORM) -> UserORM:
        """добавляю пост в user"""

        user.posts.append(post)
        self.session.add(user)
        print(user)

        return user

    async def add_posts(self, user: UserORM, posts: list[PostORM]) -> UserORM:
        """добавляю сразу несколько постов в user"""
        user.posts.extend(posts)
        self.session.add(user)

        return user
