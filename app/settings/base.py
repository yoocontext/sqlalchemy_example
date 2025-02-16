from pydantic_settings import BaseSettings
from pydantic import Field


class CommonSettings(BaseSettings):
    POSTGRES_DB: str = Field(alias="POSTGRES_DB", default="POSTGRES_DB")
    POSTGRES_USER: str = Field(alias="POSTGRES_USER", default="POSTGRES_USER")
    POSTGRES_PASSWORD: str = Field(
        alias="POSTGRES_PASSWORD", default="POSTGRES_PASSWORD"
    )
    HOST_DB: str = Field(alias="HOST_DB", default="HOST_DB")
    PORT_DB: str = Field(alias="PORT_DB", default="PORT_DB")

    @property
    def POSTGRES_URL(self) -> str:
        return rf"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.HOST_DB}:{self.PORT_DB}/{self.POSTGRES_DB}"
