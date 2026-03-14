# app/ml/model_loader.py
import random

class MLModel:

    def predict(self, age: int, income: float):
        # Fake prediction logic
        if income > 40000:
            return "approved"
        return "rejected"


model = MLModel()