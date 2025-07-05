import pandas as pd

# Load the dataset from the given path
data = pd.read_csv(r"C:\Users\hp\OneDrive\Desktop\cognify 6jun-6july\Cognifyz_Level_1_Task4\data\dataset.csv")

# Remove missing values from required columns
data = data[data['Has Online delivery'].notnull()]
data = data[data['Aggregate rating'].notnull()]

# Convert the text to lowercase to avoid mismatch
data['Has Online delivery'] = data['Has Online delivery'].str.strip().str.lower()

# Find total number of restaurants
total_restaurants = len(data)

# Find how many offer online delivery
delivery_yes = data[data['Has Online delivery'] == 'yes']
delivery_count = len(delivery_yes)

# Calculate the percentage
percentage = (delivery_count / total_restaurants) * 100

# Print the result
print(f"Percentage of Restaurants with Online Delivery: {round(percentage, 2)}%")

# Calculate average ratings based on delivery option
average_ratings = data.groupby('Has Online delivery')['Aggregate rating'].mean()

# Print comparison of ratings
print("\nAverage Ratings Comparison:")
for delivery_status, rating in average_ratings.items():
    if delivery_status == 'yes':
        label = "With Online Delivery"
    else:
        label = "Without Online Delivery"
    print(f"{label}: {round(rating, 2)}")
