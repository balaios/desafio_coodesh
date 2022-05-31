"""Space Flight News API"""

from fastapi import FastAPI

from .routers import articles

app = FastAPI()

app.include_router(articles.router)


@app.get("/")
def root():
    """Root endpoint"""
    return {"message": "Back-end Challenge 2021 🏅 - Space Flight News"}
