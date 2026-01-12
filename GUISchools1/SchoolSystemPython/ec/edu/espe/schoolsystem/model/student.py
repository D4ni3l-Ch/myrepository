class Student:

    def __init__(self, student_id, name, grade, tuition):
        self.id = student_id
        self.name = name
        self.grade = grade
        self.tuition = tuition

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_grade(self):
        return self.grade

    def get_tuition(self):
        return self.tuition
