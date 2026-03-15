# from fastapi import APIRouter
# from app.models.prediction_model import HousePredictionRequest
# from app.services.prediction_service import PredictionService

# router = APIRouter()

# @router.post("/predict")
# def predict_house_price(data: HousePredictionRequest):
#     return PredictionService.predict(
#         area=data.area,
#         bedrooms=data.bedrooms
#     )


from fastapi import APIRouter, Depends

from app.models.prediction_model import HousePredictionRequest
from app.services.prediction_service import PredictionService
from app.core.dependencies import get_prediction_service

router = APIRouter()


@router.post("/predict")
def predict(
    data: HousePredictionRequest,
    service: PredictionService = Depends(get_prediction_service)
):

    return service.predict(
        area=data.area,
        bedrooms=data.bedrooms
    )