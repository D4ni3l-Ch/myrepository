package utils;
import com.mongodb.client.MongoDatabase;
import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;

/**
 *
 * @author Daniel
 */
public class MongoDBConnection {
    
    private static MongoDatabase database;

    
    public static MongoDatabase getDatabase() {
        
        if (database == null) {
            
            MongoClient client = MongoClients.create("mongodb+srv://daniel:daniel2007@cluster0.v7buh9x.mongodb.net/?appName=Cluster0");
            database = client.getDatabase("FitnesGym");
        }
        
        return database;
    }
    
}
