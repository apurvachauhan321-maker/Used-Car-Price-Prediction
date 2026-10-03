import pandas as pd

# Load cleaned dataset
data = pd.read_csv("dataset/cleaned_cars.csv")

# Remove car name
data = data.drop("name", axis=1)

# Convert categorical columns into numbers
data = pd.get_dummies(
    data,
    columns=["fuel", "seller_type", "transmission", "owner"],
    drop_first=True
)

# Save prepared dataset
data.to_csv("dataset/prepared_cars.csv", index=False)

print("Data preparation completed!")
print("\nColumns after encoding:")
print(data.columns)

print("\nPrepared dataset shape:")
print(data.shape)