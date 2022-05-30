"""Space Flight News API"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    """Root endpoint"""
    return {"message": "Back-end Challenge 2021 🏅 - Space Flight News"}
