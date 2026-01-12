from pymongo import MongoClient

class MongoDBConnection:

    URI = "mongodb+srv://daniel:daniel2007@cluster0.v7buh9x.mongodb.net/"
    DATABASE_NAME = "school"

    @staticmethod
    def get_database():
        client = MongoClient(MongoDBConnection.URI)
        return client[MongoDBConnection.DATABASE_NAME]
