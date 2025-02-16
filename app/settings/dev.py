from functools import lru_cache
from pathlib import Path

from pydantic_settings import SettingsConfigDict

from app.settings.base import CommonSettings


class DevSettings(CommonSettings):
    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parents[2] / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache(1)
def get_settings() -> DevSettings:
    return DevSettings()
