from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.user_schema import UserRegister, UserResponse, UserLogin

from app.services.auth_service import AuthService
from app.core.dependencies import get_db

router = APIRouter()

auth_service = AuthService()


@router.post("/auth/register", response_model=UserResponse)
def register_user(
    data: UserRegister,
    db: Session = Depends(get_db)
):

    user = auth_service.register_user(
        db,
        data.username,
        data.email,
        data.password
    )

    return user

@router.post("/auth/login")
def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    service = AuthService()

    token = service.login_user(
        db,
        form_data.username,
        form_data.password
    )

    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
