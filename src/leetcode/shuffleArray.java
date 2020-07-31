package leetcode;

import java.util.Scanner;

public class shuffleArray {
    public static void main(String[]arg){
        int [] numbers = {2,5,1,3,4,7};
        int num = 3;
        for (int i = 0; i < numbers.length; i++){
            System.out.print(shuffle(numbers, num)[i] + " ");
        }
    }

    public static int[] shuffle(int[] nums, int n) {
        int first = 0;
        int second = n;
        int [] result = new int[nums.length];
        for (int i = 0; i < nums.length; i++){
            if (i % 2 == 0){
                result[i] = nums[first];
                first++;
            }
            else{
                result[i] = nums[second];
                second++;
            }
        }
        return result;
    }
}
