from pymongo import MongoClient
var url = "mongodb+srv://admin:admin@cluster0.8aucclw.mongodb.net/pytech;

client = MongoClient(url)

db = client.pytech
print(db.list_collection_names())
