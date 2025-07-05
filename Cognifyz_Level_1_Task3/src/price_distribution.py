import pandas as pd
import matplotlib.pyplot as plt
import os

# Load data from the dataset
data = pd.read_csv(r"C:\Users\hp\OneDrive\Desktop\cognify 6jun-6july\Cognifyz_Level_1_Task3\data\dataset.csv")

# Remove rows with missing 'Price range'
data = data[data['Price range'].notnull()]

# Count how many restaurants fall in each price range
price_counts = data['Price range'].value_counts().sort_index()

# Total number of restaurants (after filtering)
total_restaurants = price_counts.sum()

# Calculate percentage of restaurants in each price range
print("Percentage of Restaurants in Each Price Range:\n")
for price, count in price_counts.items():
    percent = (count / total_restaurants) * 100
    print(f"Price Range {price}: {round(percent, 2)}%")

# Show bar chart for the distribution
plt.figure(figsize=(8, 5))
plt.bar([str(i) for i in price_counts.index], price_counts.values, color='skyblue')
plt.title("Price Range Distribution of Restaurants")
plt.xlabel("Price Range")
plt.ylabel("Number of Restaurants")
plt.tight_layout()
plt.show()
