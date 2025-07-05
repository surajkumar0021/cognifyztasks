import pandas as pd
from collections import Counter
import os

# Dataset full path
file_path = r"C:\Users\hp\OneDrive\Desktop\cognify 6jun-6july\cognify_level2_task2\data\dataset.csv"

# File check
if not os.path.exists(file_path):
    print("Dataset file not found.")
    exit()

# Read the file
try:
    data = pd.read_csv(file_path)
    print("Dataset loaded successfully.")
except:
    print("Could not read the dataset.")
    exit()

# Check if columns exist
if 'Cuisines' not in data.columns or 'Aggregate rating' not in data.columns:
    print("Required columns not found in dataset.")
    exit()

# Drop missing values
data = data[['Cuisines', 'Aggregate rating']].dropna()

# Clean spaces in cuisine combinations
data['Cuisines'] = data['Cuisines'].apply(lambda x: ', '.join([c.strip() for c in x.split(',')]))

# Count most common cuisine combinations
combo_counter = Counter(data['Cuisines'])
top_combos = combo_counter.most_common(5)

# Print most common combos
print("\nMost Common Cuisine Combinations:\n")
for combo, count in top_combos:
    print(f"{combo} - {count} restaurants")

# Print average rating for each common combo
print("\nAverage Ratings of Common Cuisine Combinations:\n")
for combo, _ in top_combos:
    avg = data[data['Cuisines'] == combo]['Aggregate rating'].mean()
    print(f"{combo} - Avg Rating: {round(avg, 2)}")
