from ec.edu.espe.schoolsystem.model.student import Student
from ec.edu.espe.schoolsystem.model.student_dao import StudentDAO

class StudentController:

    def __init__(self):
        self.student_dao = StudentDAO()

    def create_student(self, student_id, name, pension):
        student = Student(student_id, name, pension)
        self.student_dao.insert(student)
