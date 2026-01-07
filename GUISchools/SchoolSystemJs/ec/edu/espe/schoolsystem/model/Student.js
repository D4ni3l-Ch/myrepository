// ec/edu/espe/schoolsystem/model/Student.js

class Student {
    constructor(id, name, grade, tuition) {
        this.id = id;
        this.name = name;
        this.grade = grade;
        this.tuition = tuition;
    }

    getId() { return this.id; }
    getName() { return this.name; }
    getGrade() { return this.grade; }
    getTuition() { return this.tuition; }
}

module.exports = Student;
