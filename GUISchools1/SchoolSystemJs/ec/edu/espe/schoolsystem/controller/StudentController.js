// ec/edu/espe/schoolsystem/controller/StudentController.js

const mongoose = require('mongoose');
const Student = require('../model/Student');

// Schema for MongoDB
const studentSchema = new mongoose.Schema({
    id: Number,
    name: String,
    grade: String,
    tuition: Number
});

// Model: explicitly use "students" collection
const StudentModel = mongoose.model('Student', studentSchema, 'students');

class StudentController {

    // Connect to MongoDB Atlas
    async connectDB() {
        try {
            await mongoose.connect(
                'mongodb+srv://daniel:daniel2007@cluster0.v7buh9x.mongodb.net/school?appName=Cluster0'
            );
            console.log('Connected to MongoDB Atlas (database: school)');
        } catch (err) {
            console.error('Error connecting to MongoDB:', err);
        }
    }

    // Generate next consecutive ID
    async getNextId() {
        const lastStudent = await StudentModel.findOne().sort({ id: -1 });
        return lastStudent ? lastStudent.id + 1 : 1;
    }

    // Create a new student
    async createStudent(name, grade, tuition) {
        const nextId = await this.getNextId();
        const student = new Student(nextId, name, grade, tuition);
        const mongoStudent = new StudentModel(student);
        await mongoStudent.save();
        console.log(`Student created with ID ${nextId}`);
    }

    // Get all students
    async getAllStudents() {
        return await StudentModel.find({}, { _id: 0, __v: 0 });
    }

    // Delete student by ID
    async deleteStudent(id) {
        const result = await StudentModel.deleteOne({ id: id });
        if (result.deletedCount === 0) {
            console.log(`No student found with ID ${id}`);
        } else {
            console.log(`Student with ID ${id} deleted`);
        }
    }

    // Calculate total tuition
    async calculateTotalIncome() {
        const students = await this.getAllStudents();
        return students.reduce((acc, s) => acc + s.tuition, 0);
    }
}

module.exports = StudentController;
