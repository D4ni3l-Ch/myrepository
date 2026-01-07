// ec/edu/espe/schoolsystem/model/Student.js
const mongoose = require('mongoose');

const studentSchema = new mongoose.Schema({
    id: Number,
    name: String,
    pension: Number
});

module.exports = mongoose.model('Student', studentSchema, 'students');
