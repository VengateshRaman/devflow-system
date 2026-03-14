# app/services/prediction_service.py

from app.ml.model_loader import model

class PredictionService:

    @staticmethod
    def predict(age, income):
        prediction = model.predict(age, income)

        return {
            "prediction": prediction
        }