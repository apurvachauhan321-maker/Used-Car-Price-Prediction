import pandas as pd

# Load dataset
data = pd.read_csv("dataset/used_cars.csv")

# Remove duplicate rows
data = data.drop_duplicates()

# Save cleaned dataset
data.to_csv("dataset/cleaned_cars.csv", index=False)

print("Data cleaning completed!")
print("Original rows: 4340")
print("Rows after removing duplicates:", len(data))
print("Cleaned dataset saved successfully!")