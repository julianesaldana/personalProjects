package leetcode;

import java.util.List;

public class kidsCandies {
    public static void main(String[]arg){
        int [] array = {2,3,5,1,3};
        int num = 3;
        for (int i = 0; i < array.length; i++)
            System.out.print(kidsWithCandies(array, num)[i] + " ");
    }

    public static boolean[] kidsWithCandies(int[] candies, int extraCandies) {
        int ctr = 0;
        int max = 0;
        boolean [] results = new boolean[candies.length];
        for (int i = 0; i < candies.length; i++){
            if (candies[i] > max)
                max = candies[i];
        }

        for (int j = 0; j < candies.length; j++){
            if (candies[j] + extraCandies >= max)
                results[j] = true;
            else
                results[j] = false;
        }
        return results;
    }
}
