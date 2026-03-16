from fastapi import APIRouter

from app.routers.v1 import health_router
# from app.routers.v1 import prediction_router

# router = APIRouter()

# router.include_router(
#     health_router.router,
#     prefix="/health",
#     tags=["Health"]
# )

# router.include_router(
#     prediction_router.router,
#     prefix="/predict",
#     tags=["Prediction"]
# )