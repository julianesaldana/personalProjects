package leetcode;

public class randomTester {
    public static void main(String[] arg) {
        int num = 3500;
        if (num % 1000 >= 1) {
            int temp = (int) (num / 1000);
            num -= temp;
        }
        System.out.println(num);
    }
}
