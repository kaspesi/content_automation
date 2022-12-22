from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

class MongoClientSingleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            print('Initializing MongoDB client...')
            MDB_USERNAME = os.getenv('MDB_USERNAME')
            MDB_PASSWORD = os.getenv('MDB_PASSWORD')
            if MDB_PASSWORD is None or MDB_USERNAME is None:
                raise Exception('MDB_USERNAME and MDB_PASSWORD must be set in .env file')
            cls.client = MongoClient(
                host = "mongodb://localhost:27017/",
                username=MDB_USERNAME,
                password=MDB_PASSWORD,
            )
            print('MongoDB client initialized.')
            database_names = cls.client.list_database_names()
            print('MongoDB databases: ' + str(database_names))
            cls._instance = super(MongoClientSingleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    # def __init__(self):
       

    def get_db(self, database_str):
        return self.client.get_database(database_str)

    def get_collection(self, database_str, collection_str):
        return self.client.get_database(database_str).get_collection(collection_str)
