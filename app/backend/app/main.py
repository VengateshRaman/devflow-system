from fastapi import FastAPI
from app.services.health_service import HealthService

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Structured Backend 🚀"}

@app.get("/health")
def health_check():
    return HealthService.get_health_status()