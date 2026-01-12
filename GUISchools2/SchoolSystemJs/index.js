const StudentController = require('./ec/edu/espe/schoolsystem/controller/StudentController');
const ConsoleView = require('./ec/edu/espe/schoolsystem/view/ConsoleView');
const MongoDBConnection = require('./ec/edu/espe/schoolsystem/utils/MongoDBConnection');

async function main() {
    const controller = new StudentController();
    const view = new ConsoleView();

    await controller.connectDB();

    let option = '';
    do {
        view.showMenu();
        option = await view.questionAsync('Select an option: ');

        switch (option) {
            case '1': {
                const idStr = await view.questionAsync('Enter ID: ');
                const studentId = parseInt(idStr);
                const name = await view.questionAsync('Enter name: ');
                const grade = await view.questionAsync('Enter grade: ');
                const tuitionStr = await view.questionAsync('Enter tuition: ');
                const tuition = parseFloat(tuitionStr);

                if (isNaN(studentId) || isNaN(tuition)) {
                    view.showMessage('ID and tuition must be numbers');
                } else {
                    await controller.createStudent(studentId, name, grade, tuition);
                }
                break;
            }
            case '2': {
                const students = await controller.getAllStudents();
                view.showStudents(students);
                break;
            }
            case '3': {
                const idStr = await view.questionAsync('Enter ID to delete: ');
                const id = parseInt(idStr);
                await controller.deleteStudent(id);
                break;
            }
            case '4': {
                const total = await controller.calculateTotalIncome();
                view.showTotal(total);
                break;
            }
            case '0':
                view.showMessage('Exiting...');
                break;
            default:
                view.showMessage('Invalid option');
        }
    } while (option !== '0');

    view.close();
    MongoDBConnection.close();
}

main();
