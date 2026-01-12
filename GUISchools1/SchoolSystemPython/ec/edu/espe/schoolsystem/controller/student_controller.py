from ec.edu.espe.schoolsystem.model.student import Student
from ec.edu.espe.schoolsystem.utils.mongodb_connection import MongoDBConnection


class StudentController:

    def __init__(self):
        db = MongoDBConnection.get_database()

        if db is None:
            raise Exception("Database connection failed")

        self.collection = db["students"]

    # ---------------- ID AUTOINCREMENT ----------------
    def _generate_id(self):
        """
        Genera un ID entero incremental
        """
        last = self.collection.find_one(sort=[("id", -1)])
        return 1 if last is None else last["id"] + 1

    # ---------------- CREATE ----------------
    def create_student(self, name, grade, tuition):
        student_id = self._generate_id()

        self.collection.insert_one({
            "id": student_id,
            "name": name,
            "grade": grade,
            "tuition": tuition
        })

    # ---------------- READ ----------------
    def get_all_students(self):
        students = []

        for doc in self.collection.find().sort("_id", 1):

            # Si el documento NO tiene id, se lo asignamos
            if "id" not in doc:
                new_id = self._generate_id()
                self.collection.update_one(
                    {"_id": doc["_id"]},
                    {"$set": {"id": new_id}}
                )
                doc["id"] = new_id

            students.append(
                Student(
                    doc["id"],
                    doc.get("name", ""),
                    doc.get("grade", ""),
                    doc.get("tuition", 0.0)
                )
            )

        return students
    # ---------------- DELETE ----------------
    def delete_student(self, student_id):
        self.collection.delete_one({"id": student_id})

    # ---------------- BUSINESS RULE ----------------
    def calculate_total_income(self):
        total = 0.0
        for doc in self.collection.find():
            total += doc["tuition"]
        return total
