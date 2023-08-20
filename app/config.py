from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

from app.constants import Environment


class Settings(BaseSettings):
    ENVIRONMENT: Environment = Environment.LOCAL
    DEBUG: bool = True
    ALLOW_ORIGINS: list[str] = ["http://localhost:3000"]

    DATABASE_URL: str = ""

    SENTRY_SDK_DSN: str = ""

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings() -> Settings:
    return Settings()
