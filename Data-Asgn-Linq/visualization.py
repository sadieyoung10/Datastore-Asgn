import matplotlib.pyplot as plt
import pandas as pd
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["my_database"]
collection = db["data"]

# Retrieve data from MongoDB
data = list(collection.find())
df = pd.DataFrame(data)

# Convert timestamp to datetime format
df['timestamp'] = pd.to_datetime(df['timestamp'])

plt.figure(figsize=(10, 6))
plt.bar(df['category'], df['value'])

#add labels and plot
plt.xlabel('Category')
plt.ylabel('Average Value')
plt.title('Average Value by Category')
plt.tight_layout()
plt.savefig('dashboard.png') 
plt.show()


#plot 2

#convert timestamp to datetime format
df['timestamp'] = pd.to_datetime(df['timestamp'])
plt.figure(figsize=(10, 6))

#loop through categories of data
for category in df['category'].unique():
    category_data = df[df['category'] == category]
    plt.plot(category_data['timestamp'], category_data['value'], label=category)

#add labels and show plot
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Value Trends Over Time by Category')
plt.legend()
plt.tight_layout()
plt.savefig('time_series_dashboard.png') 
plt.show()

