"""Database. """

import json

import httpx
from sqlmodel import Session, SQLModel, create_engine, desc, select

from ..config import settings
from ..models.articles import Article, ArticleCreate

engine = create_engine(f"{settings.db_url}")


def create_db_and_tables() -> None:
    """Create database and tables."""
    SQLModel.metadata.create_all(engine)


def get_session():
    """Get session."""
    with Session(engine) as session:
        yield session


def populate_db() -> None:
    """Populate database."""
    with Session(engine) as session:
        db_article = session.get(Article, 1)
        if not db_article:
            get_articles()


def get_articles(start: int = 0, limit: int = 200, sort: str = "id") -> None:
    """Get articles on Space Flight News API."""
    URL = "https://api.spaceflightnewsapi.net/v3/articles"
    while True:
        response = httpx.get(
            URL, params={"_start": start, "_limit": limit, "_sort": sort}
        )
        start += limit
        limit += limit
        data_json = json.loads(response.text)
        with Session(engine) as session:
            if len(data_json) != 0:
                for data in data_json:
                    article = ArticleCreate(**data)
                    db_article = Article.from_orm(article)
                    session.add(db_article)
                session.commit()
            else:
                break


def update_db() -> None:
    """Update database."""
    with Session(engine) as session:
        db_article = session.exec(select(Article).order_by(desc(Article.id))).first()
        if db_article:
            start = 0 if db_article.id is None else db_article.id
            limit = start + 200
            get_articles(start, limit)
