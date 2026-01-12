from ec.edu.espe.schoolsystem.model.student import Student
from ec.edu.espe.schoolsystem.utils.mongodb_connection import MongoDBConnection


class StudentController:

    def __init__(self):
        db = MongoDBConnection.get_database()

        if db is None:
            raise Exception("Database connection failed")

        self.collection = db["students"]

    # ---------------- CREATE ----------------
    def create_student(self, student_id, name, grade, tuition):
        """
        Crea un estudiante usando un ID ingresado por el usuario
        """
        # Verificar si el ID ya existe
        if self.collection.find_one({"id": student_id}):
            raise Exception(f"Student with ID {student_id} already exists")

        self.collection.insert_one({
            "id": student_id,
            "name": name,
            "grade": grade,
            "tuition": tuition
        })

    # ---------------- READ ----------------
    def get_all_students(self):
        """
        Retorna todos los estudiantes de la base de datos como objetos Student
        """
        students = []

        for doc in self.collection.find().sort("_id", 1):
            students.append(
                Student(
                    doc.get("id", None),
                    doc.get("name", ""),
                    doc.get("grade", ""),
                    doc.get("tuition", 0.0)
                )
            )

        return students

    # ---------------- DELETE ----------------
    def delete_student(self, student_id):
        """
        Elimina un estudiante según su ID
        """
        self.collection.delete_one({"id": student_id})

    # ---------------- BUSINESS RULE ----------------
    def calculate_total_income(self):
        """
        Suma todas las pensiones (tuition) de los estudiantes
        """
        total = 0.0
        for doc in self.collection.find():
            total += doc.get("tuition", 0.0)
        return total
