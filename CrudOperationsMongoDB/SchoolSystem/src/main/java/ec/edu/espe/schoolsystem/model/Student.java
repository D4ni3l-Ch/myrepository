package ec.edu.espe.schoolsystem.model;

/**
 *
 * @author Daniel
 */
public class Student {
    private int id;
    private String name;
    private float pension;

    public Student() {
    }

    public Student(int id, String name, float pension) {
        this.id = id;
        this.name = name;
        this.pension = pension;
    }
    
    
    /**
     * @return the id
     */
    public int getId() {
        return id;
    }

    /**
     * @param id the id to set
     */
    public void setId(int id) {
        this.id = id;
    }

    /**
     * @return the name
     */
    public String getName() {
        return name;
    }

    /**
     * @param name the name to set
     */
    public void setName(String name) {
        this.name = name;
    }

    /**
     * @return the pension
     */
    public float getPension() {
        return pension;
    }

    /**
     * @param pension the pension to set
     */
    public void setPension(float pension) {
        this.pension = pension;
    }
    
    
}
