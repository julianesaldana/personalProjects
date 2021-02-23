package leetcode;

public class validPalindrone {
    public static void main(String[] arg) {
        String example = "aabcaa";
        if (palindroneChecker(example))
            System.out.println("Palindrone");
        else
            System.out.println("Not a palindrone");
    }

    public static boolean palindroneChecker (String word){
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