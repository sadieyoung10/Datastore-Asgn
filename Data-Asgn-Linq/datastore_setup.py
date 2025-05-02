from pymongo import MongoClient

#connect to mongoDB
client = MongoClient("mongodb://localhost:27017/")

# Create or access a database and collection
db = client["my_database"]
collection = db["data"]

print("Successful")
