from sqlalchemy import Column, Integer, String
from app.core.database import Base


class Model(Base):

    __tablename__ = "models"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, unique=True)

    description = Column(String)