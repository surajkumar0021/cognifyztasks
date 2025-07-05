import pandas as pd
import os
import matplotlib.pyplot as plt

# Path to the CSV file
file_path = r"C:\Users\hp\OneDrive\Desktop\cognify 6jun-6july\cognify_level2_task3\data\dataset.csv"

# Check if file exists
if not os.path.exists(file_path):
    print("Dataset not found.")
    exit()

# Try reading the CSV
try:
    data = pd.read_csv(file_path)
    print("Data loaded successfully.")
except:
    print("Error loading the CSV file.")
    exit()

# Check if required columns are available
required_columns = ['Longitude', 'Latitude']
for col in required_columns:
    if col not in data.columns:
        print(f"Missing column: {col}")
        exit()

# Drop rows where lat or long is missing
data = data[['Latitude', 'Longitude']].dropna()

# Convert to float (some files have strings)
data['Latitude'] = pd.to_numeric(data['Latitude'], errors='coerce')
data['Longitude'] = pd.to_numeric(data['Longitude'], errors='coerce')

# Drop again if conversion failed
data = data.dropna()

print(f"Total valid restaurant locations: {len(data)}")

# Plotting location points
plt.figure(figsize=(8, 6))
plt.scatter(data['Longitude'], data['Latitude'], alpha=0.4, c='blue', s=20)

plt.title("Restaurant Locations on Map")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True)
plt.tight_layout()
plt.show()
