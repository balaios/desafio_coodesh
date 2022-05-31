"""Settings for the API."""

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Get settings"""

    db_user: str | None = None
    db_password: str | None = None
    db_host: str | None = None
    db_port: int | None = None
    db_name: str | None = None

    class Config:
        """Settings from .env"""
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
