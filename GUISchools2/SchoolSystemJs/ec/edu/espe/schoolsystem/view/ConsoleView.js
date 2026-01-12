const readline = require('readline');
const consoleTable = require('console.table');

class ConsoleView {
    constructor() {
        this.rl = readline.createInterface({
            input: process.stdin,
            output: process.stdout
        });
    }

    questionAsync(query) {
        return new Promise((resolve) => this.rl.question(query, resolve));
    }

    close() {
        this.rl.close();
    }

    showMenu() {
        console.log('\n===== SCHOOL SYSTEM MENU =====');
        console.log('1. Register student');
        console.log('2. List students');
        console.log('3. Delete student by ID');
        console.log('4. Show total tuition');
        console.log('0. Exit');
    }

    showStudents(students) {
        console.table(students, ['id', 'name', 'grade', 'tuition']);
    }

    showTotal(total) {
        console.log(`Total tuition: $${total}`);
    }

    showMessage(msg) {
        console.log(msg);
    }
}

module.exports = ConsoleView;
