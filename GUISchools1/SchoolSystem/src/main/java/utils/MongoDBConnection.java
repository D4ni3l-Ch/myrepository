package utils;

import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoDatabase;

/**
 *
 * @author Daniel
 */
public class MongoDBConnection {
        
    private static final String URI = "mongodb+srv://daniel:daniel2007@cluster0.v7buh9x.mongodb.net/?appName=Cluster0";
    
    private static MongoDatabase database;
    
    public static MongoDatabase getDataBase(){
        
        if (database == null){
            
            MongoClient client = MongoClients.create(URI);
            database = client.getDatabase("school");
        }
        
        return database;
        
    }
}
