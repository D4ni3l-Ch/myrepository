const mongoose = require('mongoose');

class MongoDBConnection {
    static async connect() {
        try {
            await mongoose.connect(
                'mongodb+srv://daniel:daniel2007@cluster0.v7buh9x.mongodb.net/school?appName=Cluster0'
            );
            console.log('Connected to MongoDB Atlas (database: school)');
        } catch (err) {
            console.error('Error connecting to MongoDB:', err);
            throw err; // para que el controlador sepa si falla
        }
    }

    static close() {
        mongoose.connection.close();
        console.log('MongoDB connection closed');
    }
}

module.exports = MongoDBConnection;
