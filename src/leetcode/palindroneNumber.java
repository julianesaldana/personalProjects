package leetcode;

import java.util.Scanner;

public class palindroneNumber {
    public static void main(String[]arg){
        Scanner in = new Scanner(System.in);
        String num = in.next();
        checker(num);
    }

    public static boolean checker(String word){
        int beginning = 0;
        int end = word.length() - 1;
        while (beginning <= end){
            if (word.charAt(beginning) != word.charAt(end))
                if (word.charAt(beginning + 1) != word.charAt(end))
                    return false;
            beginning++;
            end--;
        }
        return true;
    }
}
