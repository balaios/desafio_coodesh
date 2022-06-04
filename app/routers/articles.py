"""Routers for Articles."""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select

from ..db.database import get_session
from ..models.articles import Article, ArticleCreate, ArticleRead, ArticleUpdate

router = APIRouter()


@router.post("/articles/", response_model=ArticleRead)
def create_article(
    *,
    session: Session = Depends(get_session),
    article: ArticleCreate
):
    """Create article."""
    db_article = Article.from_orm(article)
    session.add(db_article)
    session.commit()
    session.refresh(db_article)
    return db_article


@router.get("/articles/", response_model=list[ArticleRead])
def read_articles(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
):
    """Read articles."""
    db_article = session.exec(select(Article).offset(offset).limit(limit)).all()
    return db_article


@router.get("/articles/{article_id}", response_model=ArticleRead)
def read_article(*, session: Session = Depends(get_session), article_id: int):
    """Read article."""
    db_article = session.get(Article, article_id)
    if not db_article:
        raise HTTPException(status_code=404, detail="Article not found")
    return db_article


@router.patch("/articles/{article_id}", response_model=ArticleRead)
def update_articles(
    *,
    session: Session = Depends(get_session),
    article_id: int,
    article: ArticleUpdate
):
    """Update article."""
    db_article = session.get(Article, article_id)
    if not db_article:
        raise HTTPException(status_code=404, detail="Article not found")
    article_data = article.dict(exclude_unset=True)
    for key, value in article_data.items():
        setattr(db_article, key, value)
    session.add(db_article)
    session.commit()
    session.refresh(db_article)
    return db_article


@router.delete("/articles/{article_id}")
def delete_article(*, session: Session = Depends(get_session), article_id: int):
    """Delete article."""
    db_article = session.get(Article, article_id)
    if not db_article:
        raise HTTPException(status_code=404, detail="Article not found")
    session.delete(db_article)
    session.commit()
    return {"detail": "Article deleted"}
