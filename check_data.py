import pandas as pd

data = pd.read_csv("dataset/used_cars.csv")

print("Dataset loaded successfully!")
print("\nFirst 5 rows:")
print(data.head())

print("\nDataset shape:")
print(data.shape)

print("\nColumn names:")
print(data.columns)