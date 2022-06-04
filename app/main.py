"""Space Flight News API"""

from fastapi import FastAPI

from .db.database import create_db_and_tables, populate_db
from .routers import articles

app = FastAPI()


@app.on_event("startup")
def on_startup():
    """Create table in db on startup"""
    create_db_and_tables()
    populate_db()


@app.get("/")
def root():
    """Root endpoint"""
    return {"message": "Back-end Challenge 2021 🏅 - Space Flight News"}


app.include_router(articles.router)
