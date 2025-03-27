from pymongo import MongoClient
from config import MONGO_DB_URI_1, MONGO_DB_URI_2, ENABLE_MULTI_DB

class Database:
    def __init__(self):
        self.primary_db = MongoClient(MONGO_DB_URI_1)["MainDatabase"]
        self.secondary_db = MongoClient(MONGO_DB_URI_2)["BackupDatabase"] if ENABLE_MULTI_DB else None

    def insert_data(self, collection, data):
        try:
            self.primary_db[collection].insert_one(data)
        except Exception as e:
            print(f"Primary DB Error: {e}")
            if self.secondary_db:
                self.secondary_db[collection].insert_one(data)
                print("Data stored in Secondary DB")
