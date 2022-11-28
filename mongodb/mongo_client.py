from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

class MongoClientSingleton(object):
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MongoClientSingleton, cls).__new__(cls)
        return cls._instance
        # self.dbs = self.get_dbs()
        # self.collection = self.db["customers"]

    def __init__(self):
        print('Initializing MongoDB client...')
        MDB_USERNAME = os.getenv('MDB_USERNAME')
        MDB_PASSWORD = os.getenv('MDB_PASSWORD')
        if MDB_PASSWORD is None or MDB_USERNAME is None:
            raise Exception('MDB_USERNAME and MDB_PASSWORD must be set in .env file')
        self.client = MongoClient(
            host = "mongodb://localhost:27017/",
            username=MDB_USERNAME,
            password=MDB_PASSWORD,
        )
        print('MongoDB client initialized.')
        database_names = self.client.list_database_names()
        print('MongoDB databases: ' + str(database_names))

    def get_db(self, database):
        return self.client[database]

    def get_collection(self, database, collection):
        return self.client[database][collection]

    # def get_dbs(self) -> list:
    #     dbs = {}
    #     for db in self.client.list_database_names():
    #         dbs[db] = self.client[db]