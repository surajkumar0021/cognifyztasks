import pandas as pd
import os

# Dataset location
file_path = r"C:\Users\hp\OneDrive\Desktop\cognify 6jun-6july\cognify_level2_task4\data\dataset.csv"

# Check if file is there
if not os.path.exists(file_path):
    print("Dataset not found.")
    exit()

# Try reading the file
try:
    df = pd.read_csv(file_path)
    print("Dataset loaded successfully.")
except:
    print("Error loading the dataset.")
    exit()

# Check if needed columns exist
columns_needed = ['Restaurant Name', 'Aggregate rating', 'Votes']
for col in columns_needed:
    if col not in df.columns:
        print(f"Missing column: {col}")
        exit()

# Count how many times each restaurant name appears
name_counts = df['Restaurant Name'].value_counts()

# Filter only those with more than 1 outlet = chains
chains = name_counts[name_counts > 1]

if len(chains) == 0:
    print("No restaurant chains found in the dataset.")
    exit()

# Print identified chains
print("\nIdentified Restaurant Chains:\n")
for name, count in chains.items():
    safe_name = name.encode('ascii', 'ignore').decode()
    print(f"{safe_name} - {count} outlets")

# Analyze popularity and rating of top chains (first 5 for example)
print("\nRatings and Popularity of Top 5 Chains:\n")
for name in chains.index[:5]:
    subset = df[df['Restaurant Name'] == name]
    avg_rating = subset['Aggregate rating'].mean()
    total_votes = subset['Votes'].sum()
    clean = name.encode('ascii', 'ignore').decode()
    print(f"{clean} - Avg Rating: {round(avg_rating, 2)} | Total Votes: {total_votes}")
