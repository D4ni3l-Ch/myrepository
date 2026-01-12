from pymongo import MongoClient
import os

class MongoDBConnection:
    def __init__(self):
        # URL de Mongo Atlas (puedes usar variable de entorno)
        self.mongo_url = os.getenv("mongodb+srv://daniel:daniel2007@cluster0.v7buh9x.mongodb.net/?appName=Cluster0")  # ejemplo: "mongodb+srv://user:pass@cluster0.abcde.mongodb.net/school"
        if not self.mongo_url:
            raise ValueError("Define la variable de entorno MONGO_URI con la URL de Mongo Atlas")

        # Crear cliente
        self.client = MongoClient(self.mongo_url)

    def get_database(self, db_name):
        """
        Devuelve la base de datos especificada
        """
        return self.client[db_name]