import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Fake training dataset
data = {
    "area": [1000, 1500, 2000, 2500],
    "bedrooms": [2, 3, 3, 4],
    "price": [200000, 300000, 400000, 500000]
}

df = pd.DataFrame(data)

X = df[["area", "bedrooms"]]
y = df["price"]

model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, "house_price_model.pkl")

print("Model trained and saved!")