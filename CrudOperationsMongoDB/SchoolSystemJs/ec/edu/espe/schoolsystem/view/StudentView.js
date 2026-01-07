// ec/edu/espe/schoolsystem/view/StudentView.js
const readline = require('readline-sync');
const StudentController = require('../controller/StudentController');
const MongoConnection = require('../utils/MongoConnection');

class StudentView {
    static async showMenu() {
        console.log('--- School System ---');

        let exit = false;

        while (!exit) {
            console.log('\n1. Add Student');
            console.log('0. Exit');
            const option = readline.questionInt('Select an option: ');

            switch (option) {
                case 1:
                    // Pedimos datos del estudiante
                    const id = readline.questionInt('Enter student ID: ');
                    const name = readline.question('Enter student Name: ');
                    const pension = readline.questionFloat('Enter student Pension: ');

                    // Guardamos el estudiante
                    await StudentController.create(id, name, pension);

                    
                    break;

                case 0:
                    exit = true;
                    console.log('Exiting...');
                    break;

                default:
                    console.log('Invalid option, try again.');
            }
        }
    }
}

module.exports = StudentView;
