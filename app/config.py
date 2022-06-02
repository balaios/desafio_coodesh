"""Settings for the API."""

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Get settings"""

    db_url: str | None = None

    class Config:
        """Settings from .env"""

        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
