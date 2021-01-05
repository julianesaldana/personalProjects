package leetcode;

public class addTwoNumbers {
    public static void main(String[] arg) {
        // number 2 in leetcode, wants to add numbers that are separated and reversed in a list
        int[] l1 = {2, 4, 3};
        int[] l2 = {5, 6, 4};
        String numberOne = "";
        String numberTwo = "";
        for (int i = l1.length - 1; i >= 0; i--) {
            numberOne += l1[i];
        }
        for (int i = l2.length - 1; i >= 0; i--) {
            numberTwo += l2[i];
        }
        int sum = Integer.parseInt(numberOne) + Integer.parseInt(numberTwo);
        System.out.println(sum);
    }
}
