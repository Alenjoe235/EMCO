from pymongo import MongoClient

# Create a MongoClient to the running mongod instance
client = MongoClient('localhost', 27017)

# Get a reference to a particular database
db = client['library']
collection = db['books']