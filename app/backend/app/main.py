from fastapi import FastAPI
from app.routers.api_router import api_router
from app.core.database import Base, engine
from app.models import user_model

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(api_router)