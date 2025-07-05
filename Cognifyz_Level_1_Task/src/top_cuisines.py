import pandas as pd
from collections import Counter

data = pd.read_csv(r"C:\Users\hp\OneDrive\Desktop\cognify 6jun-6july\Cognifyz_Level_1_Task\data\dataset.csv")

# Remove rows where 'Cuisines' column is empty
data = data[data['Cuisines'].notnull()]

# Create a Counter to store cuisines count
cuisine_counter = Counter()

# Count each cuisine by splitting comma-separated values
for entry in data['Cuisines']:
    split_items = entry.split(',')
    for one in split_items:
        cuisine_counter[one.strip()] += 1

# Get the top 3 cuisines
top3 = cuisine_counter.most_common(3)

# Print top 3 cuisines with their counts
print("Top 3 Most Common Cuisines:\n")
for cuisine, count in top3:
    print(f"{cuisine}: {count} restaurants")

# Calculate total number of restaurants
total_restaurants = len(data)

# Print percentage for each top cuisine
print("\nPercentage of Restaurants Serving Top Cuisines:\n")
for cuisine, count in top3:
    percentage = (count / total_restaurants) * 100
    print(f"{cuisine}: {percentage:.2f}%")
