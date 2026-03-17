from sqlalchemy import Column, Integer, String
from app.core.database import Base


class PredictionLog(Base):

    __tablename__ = "prediction_logs"

    id = Column(Integer, primary_key=True, index=True)

    model_version = Column(String)

    input_data = Column(String)

    output_data = Column(String)