import pandas as pd

data = pd.read_csv("dataset/prepared_cars.csv")

print("Prepared dataset loaded successfully!")

print("\nShape:")
print(data.shape)

print("\nColumns:")
print(data.columns.tolist())

print("\nFirst 5 rows:")
print(data.head())