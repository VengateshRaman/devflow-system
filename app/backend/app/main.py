from fastapi import FastAPI
from app.api import health

app = FastAPI()

app.include_router(health.router)

@app.get("/")
async def root():
    return {"message": "DevFlow Backend Running 🚀"}