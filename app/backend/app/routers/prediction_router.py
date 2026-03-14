# app/routers/prediction_router.py

from fastapi import APIRouter
from app.models.prediction_model import PredictionRequest
from app.services.prediction_service import PredictionService

router = APIRouter()

@router.post("/predict")
def predict(data: PredictionRequest):
    return PredictionService.predict(
        age=data.age,
        income=data.income
    )