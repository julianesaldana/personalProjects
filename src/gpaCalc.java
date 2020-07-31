import java.util.Scanner;

public class gpaCalc {
    public static void main(String[]arg){
        System.out.print("GPA Calculator\n----------\nInput number of classes you are taking: ");
        Scanner in = new Scanner(System.in);
        int numClasses = in.nextInt();
        int tally = 0;
        String grade;
        for (int i = 1; i <= numClasses; i++){
            System.out.printf("Input grade for class %d: ", i);
            grade = in.next().toUpperCase();
            switch (grade){
                case "A":
                    tally += 4;
                    break;
                case "B":
                    tally += 3;
                    break;
                case "C":
                    tally += 2;
                    break;
                case "D":
                    tally += 1;
                    break;
                case "F":
                    tally += 0;
                    break;
                default:
                    System.out.println("Must enter a letter grade A - F!");
                    break;
            }
        }
        double gpa = tally / numClasses;
        System.out.printf("Your gpa is: %.3f", gpa);
    }
}
