import joblib
from pathlib import Path

model = None

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "artifacts" / "house_price_model.pkl"


def load_model():
    global model
    model = joblib.load(MODEL_PATH)


def get_model():
    return model