import joblib
import pandas as pd

# Load the trained model
model = joblib.load("model.pkl")

print("Used Car Price Prediction")
print("-------------------------")

year = int(input("Enter car year: "))
km_driven = float(input("Enter kilometres driven: "))

fuel = input("Enter fuel type (Diesel/Petrol/CNG/LPG/Electric): ")
seller_type = input("Enter seller type (Individual/Dealer/Trustmark Dealer): ")
transmission = input("Enter transmission (Manual/Automatic): ")
owner = input("Enter owner type (First Owner/Second Owner/Third Owner/Fourth & Above Owner/Test Drive Car): ")

# Create input data
data = {
    "year": year,
    "km_driven": km_driven,
    "fuel_Diesel": 1 if fuel == "Diesel" else 0,
    "fuel_Electric": 1 if fuel == "Electric" else 0,
    "fuel_LPG": 1 if fuel == "LPG" else 0,
    "fuel_Petrol": 1 if fuel == "Petrol" else 0,
    "seller_type_Individual": 1 if seller_type == "Individual" else 0,
    "seller_type_Trustmark Dealer": 1 if seller_type == "Trustmark Dealer" else 0,
    "transmission_Manual": 1 if transmission == "Manual" else 0,
    "owner_Fourth & Above Owner": 1 if owner == "Fourth & Above Owner" else 0,
    "owner_Second Owner": 1 if owner == "Second Owner" else 0,
    "owner_Test Drive Car": 1 if owner == "Test Drive Car" else 0,
    "owner_Third Owner": 1 if owner == "Third Owner" else 0
}

input_data = pd.DataFrame([data])

# Predict price
prediction = model.predict(input_data)

print()
print("Predicted Car Price: ₹", round(prediction[0], 2))