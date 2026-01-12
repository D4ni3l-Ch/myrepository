// index.js

const readline = require('readline');
const mongoose = require('mongoose');
const StudentController = require('./ec/edu/espe/schoolsystem/controller/StudentController');
const consoleTable = require('console.table');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const controller = new StudentController();

// Menu function
function showMenu() {
    console.log('\n===== SCHOOL SYSTEM MENU =====');
    console.log('1. Register student');
    console.log('2. List students');
    console.log('3. Delete student by ID');
    console.log('4. Show total tuition');
    console.log('0. Exit');
}

// Readline promise
function questionAsync(query) {
    return new Promise((resolve) => rl.question(query, resolve));
}

// Main function
async function main() {
    await controller.connectDB();

    let option = '';
    do {
        showMenu();
        option = await questionAsync('Select an option: ');

        switch (option) {
            case '1': {
                const name = await questionAsync('Enter name: ');
                const grade = await questionAsync('Enter grade: ');
                const tuitionStr = await questionAsync('Enter tuition: ');
                const tuition = parseFloat(tuitionStr);
                await controller.createStudent(name, grade, tuition);
                break;
            }
            case '2': {
                const students = await controller.getAllStudents();
                console.table(students, ['id', 'name', 'grade', 'tuition']);
                break;
            }
            case '3': {
                const idStr = await questionAsync('Enter ID to delete: ');
                const id = parseInt(idStr);
                await controller.deleteStudent(id);
                break;
            }
            case '4': {
                const total = await controller.calculateTotalIncome();
                console.log(`Total tuition: $${total}`);
                break;
            }
            case '0':
                console.log('Exiting...');
                break;
            default:
                console.log('Invalid option');
        }
    } while (option !== '0');

    rl.close();
    mongoose.connection.close();
}

main();
