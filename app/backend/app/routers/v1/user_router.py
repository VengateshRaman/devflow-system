from fastapi import APIRouter, Depends

from app.models.user_model import User
from app.core.dependencies import get_current_user
from app.schemas.user_schema import UserResponse

router = APIRouter()

@router.get("/users")
def get_users():
    return {"users": []}


@router.get("/users/me", response_model=UserResponse)
def get_current_user_profile(
    current_user: User = Depends(get_current_user)
):

    return current_user