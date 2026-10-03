import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Load prepared dataset
data = pd.read_csv("dataset/prepared_cars.csv")

# Features and target
X = data.drop("selling_price", axis=1)
y = data["selling_price"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Gradient Boosting model
model = GradientBoostingRegressor(
    n_estimators=200,
    learning_rate=0.05,
    max_depth=3,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Evaluate
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("Gradient Boosting training completed!")
print("Mean Absolute Error:", round(mae, 2))
print("R² Score:", round(r2, 4))
import joblib

joblib.dump(model, "model.pkl")

print("Model saved successfully!")