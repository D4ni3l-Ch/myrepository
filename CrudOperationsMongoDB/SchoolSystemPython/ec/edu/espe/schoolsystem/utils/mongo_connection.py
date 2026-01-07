from pymongo import MongoClient

class MongoConnection:

    @staticmethod
    def get_database():
        client = MongoClient("mongodb+srv://daniel:daniel2007@cluster0.v7buh9x.mongodb.net/?appName=Cluster0")
        return client["school"]
