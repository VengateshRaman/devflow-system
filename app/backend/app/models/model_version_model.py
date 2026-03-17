from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.database import Base


class ModelVersion(Base):

    __tablename__ = "model_versions"

    id = Column(Integer, primary_key=True, index=True)

    model_id = Column(Integer, ForeignKey("models.id"))

    version = Column(String)

    path = Column(String)

    status = Column(String)