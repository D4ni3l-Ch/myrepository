package ec.edu.espe.schoolsystem.controller;

import ec.edu.espe.schoolsystem.model.Student;
import ec.edu.espe.schoolsystem.model.StudentDAO;

/**
 *
 * @author Daniel
 */
public class StudentController {
    
    private StudentDAO studentDAO;

    public StudentController() {
        studentDAO = new StudentDAO();
    }

    public void createStudent(int id, String name, float pension) {

        if (id <= 0) {
            System.out.println("Invalid ID");
            return;
        }

        Student student = new Student(id, name, pension);
        studentDAO.insert(student);
    }
    
}
