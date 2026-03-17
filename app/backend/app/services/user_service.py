from sqlalchemy.orm import Session
from app.models.user_model import User


class UserService:

    def get_all_users(self, db: Session):
        return db.query(User).all()

    def get_user_by_id(self, db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()

    def get_user_by_email(self, db: Session, email: str):
        return db.query(User).filter(User.email == email).first()