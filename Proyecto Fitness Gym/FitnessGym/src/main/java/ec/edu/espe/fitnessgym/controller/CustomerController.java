package ec.edu.espe.fitnessgym.controller;

import com.mongodb.client.MongoCollection;
import ec.edu.espe.fitnessgym.model.Customer;
import java.util.ArrayList;
import java.util.List;
import utils.MongoDBConnection;
import org.bson.Document;
/**
 *
 * @author Daniel
 */
public class CustomerController {
    
    private MongoCollection<Document> collection;
     
    public CustomerController(){
         
        collection = MongoDBConnection.getDatabase().getCollection("Customers");
         
    }
     
    public void createCustomer(Customer customer){
        
        Document document = new Document().append("id",customer.getId()).append("name", customer.getName()).append("age", customer.getAge()).append("weight", customer.getWeight()).append("height", customer.getHeight());
        
        collection.insertOne(document);
        
    }
    
    public List<Customer> findAllCustomers() {

        List<Customer> customers = new ArrayList<>();

        for (Document doc : collection.find()) {

            Customer customer = new Customer();

            customer.setId(((Number) doc.get("id")).intValue());
            customer.setName(doc.getString("name"));
            customer.setAge(((Number) doc.get("age")).intValue());
            customer.setWeight(((Number) doc.get("weight")).floatValue());
            customer.setHeight(((Number) doc.get("height")).floatValue());

            customers.add(customer);
        }

        return customers;
    }

    public List<Float> calculateBMIForCustomers(List<Customer> customers) {

        List<Float> bmiList = new ArrayList<>();

        for (Customer c : customers) {
            float bmi = 0f;

            if (c.getHeight() > 0) { // evitamos división por cero
                bmi = c.getWeight() / (c.getHeight() * c.getHeight());
            }

            bmiList.add(bmi);
        }

        return bmiList;
    }
    
    public float calculateTotalWeightHeight(List<Customer> customers) {

        float total = 0f; // acumulador

        for (Customer c : customers) {
            total += c.getWeight() * c.getHeight();
        }

        return total; // devuelve el total final
    }
}   
