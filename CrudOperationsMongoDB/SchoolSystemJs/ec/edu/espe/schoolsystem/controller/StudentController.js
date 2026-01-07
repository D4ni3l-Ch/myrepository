// ec/edu/espe/schoolsystem/controller/StudentController.js
const Student = require('../model/Student');

class StudentController {
    static async create(id, name, pension) {
        const student = new Student({ id, name, pension });
        await student.save();
        console.log('Student saved successfully');
    }

    static async getAll() {
        return await Student.find();
    }
}

module.exports = StudentController;
