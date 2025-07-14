
from pymongo.mongo_client import MongoClient # type: ignore

uri = "mongodb+srv://raunakgupta914:rowdy123@networksecurity.4afnsvt.mongodb.net/?retryWrites=true&w=majority&appName=networksecurity"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)