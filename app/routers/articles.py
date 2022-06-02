"""Routers for Articles."""

from fastapi import APIRouter

from ..models.articles import Article

router = APIRouter()


@router.get("/articles/")
async def get_articles():
    """Function to get articles from the space flightnews API"""
    return {"message": "Get articles is not supported yet."}


@router.post("/articles/")
async def post_article():
    """Function to post articles from the space flightnews API"""
    return {"message": "Posting articles is not supported yet."}


@router.get("/articles/{id}")
async def get_article():
    """Function to get articles from the space flightnews API"""
    return {"message": "Get article is not supported yet."}


@router.put("/articles/{id}")
async def put_article():
    """Function to put articles from the space flightnews API"""
    return {"message": "Putting articles is not supported yet."}


@router.delete("/articles/{id}")
async def delete_article():
    """Function to delete articles from the space flightnews API"""
    return {"message": "Deleting articles is not supported yet."}
