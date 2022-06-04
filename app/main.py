"""Space Flight News API"""

from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import FastAPI

from .db.database import create_db_and_tables, populate_db, update_db
from .routers import articles

app = FastAPI()


@app.on_event("startup")
def on_startup():
    """Create table, populate and add cronjob to update db on startup"""
    create_db_and_tables()
    populate_db()
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_db, "cron", hour=9, timezone="America/Sao_Paulo")
    scheduler.start()


@app.get("/")
def root():
    """Root endpoint"""
    return {"message": "Back-end Challenge 2021 🏅 - Space Flight News"}


app.include_router(articles.router)
