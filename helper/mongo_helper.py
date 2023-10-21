# mongo_helper.py

import pymongo

class MongoDBHelper:
    def __init__(self, connection_string):
        self.client = pymongo.MongoClient(connection_string)
        self.db = self.client.get_default_database()

    def upload_to_mongodb(self, json_data, collection_name):
        collection = self.db[collection_name]
        collection.insert_many(json_data)
