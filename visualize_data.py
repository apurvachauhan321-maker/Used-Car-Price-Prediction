import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
data = pd.read_csv("dataset/cleaned_cars.csv")

# 1. Selling Price Distribution
plt.figure(figsize=(8, 5))
sns.histplot(data["selling_price"], bins=30)
plt.title("Distribution of Used Car Prices")
plt.xlabel("Selling Price")
plt.ylabel("Number of Cars")
plt.show()

# 2. Cars by Fuel Type
plt.figure(figsize=(7, 5))
sns.countplot(x="fuel", data=data)
plt.title("Cars by Fuel Type")
plt.xlabel("Fuel Type")
plt.ylabel("Number of Cars")
plt.show()

# 3. Selling Price vs Year
plt.figure(figsize=(8, 5))
sns.scatterplot(x="year", y="selling_price", data=data)
plt.title("Selling Price vs Year")
plt.xlabel("Year")
plt.ylabel("Selling Price")
plt.show()

# 4. Selling Price vs Kilometres Driven
plt.figure(figsize=(8, 5))
sns.scatterplot(x="km_driven", y="selling_price", data=data)
plt.title("Selling Price vs Kilometres Driven")
plt.xlabel("Kilometres Driven")
plt.ylabel("Selling Price")
plt.show()