from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session


from fastapi.security import OAuth2PasswordBearer

from app.services.prediction_service import PredictionService
from app.core.database import SessionLocal
from app.core.security import verify_token
from app.models.user_model import User


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/auth/login")


def get_prediction_service():
    return PredictionService()

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    email = verify_token(token)

    user = db.query(User).filter(User.email == email).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user