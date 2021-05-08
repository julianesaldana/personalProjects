package leetcode;

import java.util.LinkedList;

public class addTwoNumbers {
    // FIXME: this works only for regular arrays
//    public static void main(String[] arg) {
//        int[] l1 = {2, 4, 3};
//        int[] l2 = {5, 6, 4};
//        String numberOne = "";
//        String numberTwo = "";
//        for (int i = l1.length - 1; i >= 0; i--) {
//            numberOne += l1[i];
//        }
//        for (int i = l2.length - 1; i >= 0; i--) {
//            numberTwo += l2[i];
//        }
//        int sum = Integer.parseInt(numberOne) + Integer.parseInt(numberTwo);
//        System.out.println(sum);
//    }

    public static void main(String[] arg) {
        // two numbers that will be parsed later
        String firstNum = "";
        String secondNum = "";
        // generating first linked list and adding values
        LinkedList<Integer> firstList = new LinkedList<Integer>();
        firstList.add(2); firstList.add(4); firstList.add(3);
        // generating second linked list and adding values
        LinkedList<Integer> secondList = new LinkedList<Integer>();
        secondList.add(5); secondList.add(6); secondList.add(4);

        // two for loops that will reverse iterate throught the lists
        for (int i = firstList.size() - 1; i >= 0; i--) {

        }
        for (Integer temp : secondList )
            secondNum += temp;

        System.out.println(firstNum);
        System.out.println(secondNum);

        int sum = Integer.parseInt(firstNum) + Integer.parseInt(secondNum);
    }
}
