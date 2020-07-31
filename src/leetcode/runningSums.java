package leetcode;


public class runningSums {
    public static void main(String[]arg){
        int [] test = {1,2,3,4};
        int [] results = runningSum(test);
        for (int i = 0; i < test.length; i++)
            System.out.print(results[i] + " ");
    }


    public static int[] runningSum(int[] nums) {
        int [] result = new int[nums.length];
        result[0] = nums[0];
        for (int i = 1; i < nums.length; i++){
            result[i] = result[i - 1] + nums[i];
        }
        return result;
    }
}
