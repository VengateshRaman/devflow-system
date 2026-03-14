from fastapi import FastAPI
from app.core.config import settings
from app.routers import health_router
from app.routers import prediction_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION
)

app.include_router(health_router.router)
app.include_router(prediction_router.router)