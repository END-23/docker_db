from pymongo import MongoClient

# MongoDB connection
client = MongoClient('mongo', 27017)
db = client['mydatabase']
collection = db['database']

# Find and print all documents
for doc in collection.find():
    print(doc)

# Close MongoDB connection
client.close()
