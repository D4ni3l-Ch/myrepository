package ec.edu.espe.schoolsystem.model;

/**
 *
 * @author Daniel
 */
public class Student {
    private int id;
    private String name;
    private String grade;
    private double tuition;

    public Student() {
    }
    
    
    public Student(int id, String name, String grade, double tuition) {
        this.id = id;
        this.name = name;
        this.grade = grade;
        this.tuition = tuition;
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
     * @return the grade
     */
    public String getGrade() {
        return grade;
    }

    /**
     * @param grade the grade to set
     */
    public void setGrade(String grade) {
        this.grade = grade;
    }

    /**
     * @return the tuition
     */
    public double getTuition() {
        return tuition;
    }

    /**
     * @param tuition the tuition to set
     */
    public void setTuition(double tuition) {
        this.tuition = tuition;
    }

    
    
}
