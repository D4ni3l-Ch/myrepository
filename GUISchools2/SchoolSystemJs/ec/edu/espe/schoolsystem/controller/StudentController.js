const Student = require('../model/Student');
const mongoose = require('mongoose');
const MongoDBConnection = require('../utils/MongoDBConnection');

const studentSchema = new mongoose.Schema({
    id: Number,
    name: String,
    grade: String,
    tuition: Number
});

const StudentModel = mongoose.model('Student', studentSchema, 'students');

class StudentController {

    async connectDB() {
        await MongoDBConnection.connect();
    }

    // Ahora el ID es **ingresado por el usuario**
    async createStudent(studentId, name, grade, tuition) {
        const student = new Student(studentId, name, grade, tuition);
        const mongoStudent = new StudentModel(student);
        await mongoStudent.save();
        console.log(`Student created with ID ${studentId}`);
    }

    async getAllStudents() {
        return await StudentModel.find({}, { _id: 0, __v: 0 });
    }

    async deleteStudent(id) {
        const result = await StudentModel.deleteOne({ id: id });
        if (result.deletedCount === 0) {
            console.log(`No student found with ID ${id}`);
        } else {
            console.log(`Student with ID ${id} deleted`);
        }
    }

    async calculateTotalIncome() {
        const students = await this.getAllStudents();
        return students.reduce((acc, s) => acc + s.tuition, 0);
    }
}

module.exports = StudentController;
