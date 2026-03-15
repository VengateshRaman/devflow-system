from pydantic import BaseModel

class HousePredictionRequest(BaseModel):
    area: int
    bedrooms: int


class HousePredictionResponse(BaseModel):
    predicted_price: float