package leetcode;

public class twoSum {
    public static void main(String[]arg) {
        int target = 9;
        int [] nums = {1, 4, 5, 2};
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    System.out.printf("%d and %d together make %d", nums[i], nums[j], target);
                }
            }
        }
    }
}
