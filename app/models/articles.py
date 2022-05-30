"""Models for Article."""

from sqlmodel import JSON, Column, Field, SQLModel


class Article(SQLModel, table=True):
    """Validation and serialization for Article."""

    id: None | int = Field(default=None, primary_key=True)
    title: str
    url: str
    imageUrl: str
    newsSite: str
    summary: str
    publishedAt: str
    updatedAt: str
    featured: bool
    launches: list[dict[str, str]] = Field(sa_column=Column(JSON))
    events: list[dict[str, str]] = Field(sa_column=Column(JSON))
