import pandas as pd
from collections import Counter
import os

# Full file path to the dataset
file_path = r"C:\Users\hp\OneDrive\Desktop\cognify 6jun-6july\cognifyz_level_2_task1\data\dataset.csv"

# Check if the file exists
if not os.path.exists(file_path):
    print("File not found at given path")
    exit()

# Try to read the dataset
try:
    data = pd.read_csv(file_path)
    print("File loaded successfully")
except:
    print("Could not read the file")
    exit()

# Select necessary columns
if 'Aggregate rating' not in data.columns or 'Votes' not in data.columns:
    print("Required columns are missing in the file")
    exit()

# Filter and clean data
df = data[['Aggregate rating', 'Votes']].dropna()
df['Votes'] = pd.to_numeric(df['Votes'], errors='coerce')
df = df[df['Votes'].notnull()]

print(f"\nTotal number of restaurants analyzed: {len(df)}")

# Find the most common rating
rating_counts = Counter(df['Aggregate rating'].tolist())
common_rating = rating_counts.most_common(1)[0]
print(f"\nMost common rating: {common_rating[0]} (appeared {common_rating[1]} times)")

# Calculate average number of votes
avg_votes = df['Votes'].mean()
print(f"\nAverage number of votes per restaurant: {round(avg_votes, 2)}")

# Calculate percentage of restaurants with rating >= 4
high_rated = df[df['Aggregate rating'] >= 4]
percentage_high = (len(high_rated) / len(df)) * 100
print(f"\nPercentage of restaurants rated 4 or above: {round(percentage_high, 1)}%")
