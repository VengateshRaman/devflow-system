from fastapi import HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from app.models.user_model import User
from app.core.security import create_access_token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthService:

    def register_user(self, db: Session, username: str, email: str, password: str):

        hashed_password = pwd_context.hash(password[:72])

        user = User(
            username=username,
            email=email,
            password=hashed_password
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return user
    
    def login_user(self, db: Session, email: str, password: str):

        user = db.query(User).filter(User.email == email).first()

        if not user:
            raise HTTPException(status_code=401, detail="Invalid email")

        if not pwd_context.verify(password, user.password):
            raise HTTPException(status_code=401, detail="Invalid password")

        token = create_access_token(
            data={"sub": user.email}
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }