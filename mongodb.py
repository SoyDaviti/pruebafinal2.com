from pymongo.mongo_client import MongoClient
import certifi
import os
from dotenv import load_dotenv

load_dotenv()

user = os.getenv("MONGO_USER")
password = os.getenv("MONGO_PASSWORD")
db_hostname = os.getenv("MONGO_HOST")
uri = f"mongodb+srv://{user}:{password}@{db_hostname}/?retryWrites=true&w=majority"
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(uri, tlsCAFile=ca)
        db = client["autos"]
    except ConnectionError:
        print('Error de conexion BD')
    return db










#class MongoConnection:
#    def __init__(self):
#        user = os.getenv("MONGO_USER")
#        password = os.getenv("MONGO_PASSWORD")
#        db_hostname = os.getenv("MONGO_HOST")
#        uri = f"mongodb+srv://{user}:{password}@{db_hostname}/?retryWrites=true&w=majority"

        # Create a new client and connect to the server
#        self.client = MongoClient(uri, server_api=ServerApi('1'))
        ##ca = certifi.where()
    # Send a ping to confirm a successful connection
#    def test_connection(self):
#        try:
#            self.client.admin.command('ping')
#            print("Pinged your deployment. You successfully connected to MongoDB!")
#        except Exception as e:
#            print(e)

#if __name__ == "__main__":
#    MongoConnection().test_connection()
