import pandas as pd

# 📌 Load the dataset using the full path
data = pd.read_csv(r"C:\Users\hp\OneDrive\Desktop\cognify 6jun-6july\Cognifyz_Level_1_Task2\data\dataset.csv")

# 📌 Remove missing values from City and Rating
data = data[data['City'].notnull()]
data = data[data['Aggregate rating'].notnull()]

# 📌 Find the city with the most restaurants
city_counts = data['City'].value_counts()
top_city = city_counts.idxmax()
top_count = city_counts.max()

print("City with the highest number of restaurants:")
print(f"{top_city} - {top_count} restaurants")

# 📌 Calculate average rating for each city
avg_rating_city = data.groupby('City')['Aggregate rating'].mean()

# 📌 Sort cities by average rating
sorted_avg = avg_rating_city.sort_values(ascending=False)

print("\nTop 10 Cities by Average Rating:\n")
print(sorted_avg.head(10))

# 📌 City with highest average rating
best_city = sorted_avg.idxmax()
best_rating = sorted_avg.max()

print(f"\nCity with the highest average rating: {best_city} ({round(best_rating, 2)})")
