"""Space Flight News API"""

from fastapi import FastAPI

from .db.database import create_db_and_tables
from .routers import articles

app = FastAPI()


@app.on_event("startup")
def startup():
    """Create table in db on startup"""
    create_db_and_tables()


@app.get("/")
def root():
    """Root endpoint"""
    return {"message": "Back-end Challenge 2021 🏅 - Space Flight News"}


app.include_router(articles.router)
