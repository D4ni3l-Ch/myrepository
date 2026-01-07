
package ec.edu.espe.schoolsystem.model;

import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import utils.MongoDBConnection;
import org.bson.Document;


/**
 *
 * @author Daniel
 */
public class StudentDAO {
    
    private MongoCollection<Document> collection;
      
    public   StudentDAO(){
        
        MongoDatabase database = MongoDBConnection.getDatabase();
        collection = database.getCollection("students");
        
    }
    
    public void insert (Student student){
        Document document = new Document("id",student.getId()).append("name", student.getName()).append("pension",student.getPension());
        collection.insertOne(document);
        
  
    }
    
}
