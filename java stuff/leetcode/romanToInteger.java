package leetcode;

import java.util.Scanner;

public class romanToInteger {
    public static void main(String[]arg){
        System.out.println("Enter a roman numeral");
        Scanner in = new Scanner(System.in);
        String roman = in.nextLine();
        System.out.println(romanToInt(roman));
    }

    public static int romanToInt(String s) {
        int value = 0;
        for (int i = 0; i < s.length(); i++){
            if (i != s.length() - 1 && s.charAt(i) == 'I' && (s.charAt(i + 1) == 'V' || s.charAt(i + 1) == 'X'))
                value--;
            else if (s.charAt(i) == 'I')
                value++;
            if (s.charAt(i) == 'V')
                value += 5;
            if (i != s.length() - 1 && s.charAt(i) == 'X' && (s.charAt(i + 1) == 'L' || s.charAt(i + 1) == 'C'))
                value -= 10;
            else if (s.charAt(i) == 'X')
                value += 10;
            if (s.charAt(i) == 'L')
                value += 50;
            if (i != s.length() - 1 && s.charAt(i) == 'C' && (s.charAt(i + 1) == 'D' || s.charAt(i + 1) == 'M'))
                value -= 100;
            else if (s.charAt(i) == 'C')
                value += 100;
            if (s.charAt(i) == 'D')
                value += 500;
            if (s.charAt(i) == 'M')
                value += 1000;
        }
        return value;
    }
}
