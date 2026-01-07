from ec.edu.espe.schoolsystem.utils.mongo_connection import MongoConnection

class StudentDAO:

    def __init__(self):
        db = MongoConnection.get_database()
        self.collection = db["students"]

    def insert(self, student):
        document = {
            "id": student.id,
            "name": student.name,
            "pension": student.pension
        }
        self.collection.insert_one(document)
