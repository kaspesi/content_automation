from pymongo import MongoClient

class MongoClient:

    def __new__(self, database) -> None:
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client[database]
        # self.dbs = self.get_dbs()
        # self.collection = self.db["customers"]

    def db(self):
        return self.db

    # def get_dbs(self) -> list:
    #     dbs = {}
    #     for db in self.client.list_database_names():
    #         dbs[db] = self.client[db]