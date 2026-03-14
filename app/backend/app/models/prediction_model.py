# app/models/prediction_model.py

from pydantic import BaseModel

class PredictionRequest(BaseModel):
    age: int
    income: float


class PredictionResponse(BaseModel):
    prediction: str