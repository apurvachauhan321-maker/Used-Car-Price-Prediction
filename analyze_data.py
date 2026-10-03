import pandas as pd

data = pd.read_csv("dataset/used_cars.csv")

print("Missing values:")
print(data.isnull().sum())

print("\nDuplicate rows:")
print(data.duplicated().sum())

print("\nBasic statistics:")
print(data.describe())

print("\nFuel types:")
print(data["fuel"].value_counts())

print("\nTransmission types:")
print(data["transmission"].value_counts())

print("\nOwner types:")
print(data["owner"].value_counts())