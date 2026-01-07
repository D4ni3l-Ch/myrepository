// ec/edu/espe/schoolsystem/utils/MongoConnection.js
const mongoose = require('mongoose');

class MongoConnection {
    static async connect() {
        try {
            await mongoose.connect(
                'mongodb+srv://daniel:daniel2007@cluster0.v7buh9x.mongodb.net/school?appName=Cluster0'
            );
            console.log('MongoDB connected');
        } catch (error) {
            console.error('MongoDB connection error:', error.message);
        }
    }
}

module.exports = MongoConnection;
