"""Database. """
from sqlmodel import SQLModel, create_engine

from ..config import settings

engine = create_engine(f"{settings.db_url}")


def create_db_and_tables():
    """Create database and tables."""
    SQLModel.metadata.create_all(engine)
