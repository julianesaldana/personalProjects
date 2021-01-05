import java.util.*;

public class moneyCalc {
    public static void main(String[]arg){
        Scanner in = new Scanner(System.in);
        System.out.println("how many 100s?");
        int hundreds = in.nextInt();
        System.out.println("how many 50s?");
        int fiftys = in.nextInt();
        System.out.println("how many 20s?");
        int twentys = in.nextInt();
        System.out.println("how many 10s?");
        int tens = in.nextInt();
        System.out.println("how many 5s?");
        int fives = in.nextInt();
        System.out.println("how many 1s?");
        int ones = in.nextInt();

        int total = (100 * hundreds) + (50 * fiftys) + (20 * twentys) + (10 * tens) + (5 * fives) + (ones);
        System.out.printf("Your total amount of money is %d", total);
    }
}
