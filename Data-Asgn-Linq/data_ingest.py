from datetime import datetime
from pymongo import MongoClient

#connect to mongoDB and clear previous data
client = MongoClient("mongodb://localhost:27017/")
db = client["my_database"]
collection = db["data"]
collection.delete_many({})

# Hardcoded categories, values, and timestamps and insert into mongoDB
data = [
    {"category": "Product A", "value": 50, "timestamp": "2025-04-20T10:00:00"},
    {"category": "Product B", "value": 75, "timestamp": "2025-04-21T12:00:00"},
    {"category": "Product A", "value": 30, "timestamp": "2025-04-22T09:00:00"},
    {"category": "Product C", "value": 40, "timestamp": "2025-04-23T11:00:00"},
    {"category": "Product B", "value": 60, "timestamp": "2025-04-24T14:00:00"},
    {"category": "Product C", "value": 20, "timestamp": "2025-04-25T16:00:00"},
    {"category": "Product A", "value": 90, "timestamp": "2025-04-26T13:00:00"},
    {"category": "Product B", "value": 50, "timestamp": "2025-04-27T18:00:00"},
    {"category": "Product C", "value": 70, "timestamp": "2025-04-28T15:00:00"},
    {"category": "Product A", "value": 80, "timestamp": "2025-04-29T17:00:00"}
]

collection.insert_many(data)

print("Data inserted")