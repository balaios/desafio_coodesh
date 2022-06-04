"""Models for Article."""

from sqlmodel import JSON, Column, Field, SQLModel


class ArticleBase(SQLModel):
    """Validation and serialization for Article."""

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


class Article(ArticleBase, table=True):
    """Article model."""

    id: int | None = Field(default=None, primary_key=True)


class ArticleCreate(ArticleBase):
    """Article create model."""


class ArticleRead(ArticleBase):
    """Article read model."""

    id: int


class ArticleUpdate(SQLModel):
    """Article update model."""

    title: str | None = None
    url: str | None = None
    imageUrl: str | None = None
    newsSite: str | None = None
    summary: str | None = None
    publishedAt: str | None = None
    updatedAt: str | None = None
    featured: bool | None = None
    launches: list[dict[str, str]] | None = Field(sa_column=Column(JSON))
    events: list[dict[str, str]] | None = Field(sa_column=Column(JSON))
