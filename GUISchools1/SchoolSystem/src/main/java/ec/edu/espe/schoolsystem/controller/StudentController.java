package ec.edu.espe.schoolsystem.controller;

import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import static com.mongodb.client.model.Filters.eq;
import com.mongodb.client.model.FindOneAndUpdateOptions;
import com.mongodb.client.model.ReturnDocument;
import static com.mongodb.client.model.Updates.inc;
import ec.edu.espe.schoolsystem.model.Student;
import org.bson.Document;
import utils.MongoDBConnection;

import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author Daniel
 */
public class StudentController {
  
    private final MongoCollection<Document> collection ;
    
    
    private int getNextStudentId() {
        
        Document result = collection.find().sort(new Document("id", -1)).first();

        if (result == null) {
            return 1; 
        }

        return result.getInteger("id") + 1;
    }
    
    public StudentController(){
        
        MongoDatabase db = MongoDBConnection.getDataBase();
        collection = db.getCollection("students");
    }
    
    
    public void createStudent(Student student){
        int newId= getNextStudentId();
        
        Document doc = new Document("id",newId).append("name",student.getName()).append("grade", student.getGrade()).append("tuition",student.getTuition());
        collection.insertOne(doc);
        
    }
    
    public List<Student> getAllStudents(){
        
        List <Student> students = new ArrayList<>();
        
        for (Document doc : collection.find()){
            Student  s= new Student(doc.getInteger("id"),doc.getString("name"),doc.getString("grade"),doc.getDouble("tuition"));
            students.add(s);   
        }
        return students;
    }    
    
    public boolean deleteStudentById(int id) {

        Document filter = new Document("id", id);
        return collection.deleteOne(filter).getDeletedCount() > 0;
    }
    
    
    public double calculateTotalIncome(){
        
        double total=0;
        
        for (Document doc : collection.find()){
            total += doc.getDouble("tuition");
            
        }
        return total;
    }
    
    
}
