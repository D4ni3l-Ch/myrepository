// ec/edu/espe/schoolsystem/main.js
const MongoConnection = require('./ec/edu/espe/schoolsystem/utils/MongoConnection');
const StudentView = require('./ec/edu/espe/schoolsystem/view/StudentView');

async function main() {
    // Conectamos a MongoDB
    await MongoConnection.connect();

    // Mostramos el menú de estudiantes
    await StudentView.showMenu();
}

main();


  /*Ejecutar con "node ec\edu\espe\schoolsystem\main.js  */