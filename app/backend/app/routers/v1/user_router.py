from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models.user_model import User
from app.schemas.user_schema import UserResponse
from app.core.dependencies import get_current_user, get_db
from app.services.user_service import UserService

router = APIRouter()

user_service = UserService()


@router.get("/users")
def get_users(db: Session = Depends(get_db)):

    users = user_service.get_all_users(db)

    return users


@router.get("/users/me", response_model=UserResponse)
def get_current_user_profile(
    current_user: User = Depends(get_current_user)
):

    return current_user