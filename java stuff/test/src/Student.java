public class Student {
    public static int counter = 1;
    private String name;
    private int id;
    private double gpa;

    public Student(String studentName, double givenGPA) {
        name = studentName;
        id = counter++;
        gpa = givenGPA;
    }

    public void display(){
        System.out.println("Name: " + name + ", ID number: " + id + ", GPA: " + gpa);
    }
}
