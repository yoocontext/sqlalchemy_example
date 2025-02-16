from abc import ABC, abstractmethod
from dataclasses import dataclass

from sqlalchemy.ext.asyncio import AsyncSession


@dataclass
class BaseRepositoryORM(ABC):
    session: AsyncSession

    @abstractmethod
    async def get_by_id(self, required_id: int): ...
