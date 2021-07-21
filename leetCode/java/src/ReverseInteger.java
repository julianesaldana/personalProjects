public class ReverseInteger {
    static int reverse(int x) {
        if (x == 0)
            return 0;
        boolean isNegative = x < 0;
        if (isNegative)
            x *= -1;
        String newNum = "";
        while (x > 0) {
            newNum += x % 10;
            x = x / 10;
        }
        long tempResult = Long.parseLong(newNum);
        System.out.println(tempResult);
        if (tempResult > Integer.MAX_VALUE)
            return 0;
        else {
            int result = Integer.parseInt(newNum);
            if (isNegative)
                result *= -1;
            return result;
        }
    }

    public static void main(String[] arg) {
//        int leetcodeNum = 9646324351;
        System.out.println(Integer.MAX_VALUE);
        int maxInt = Integer.MAX_VALUE;
        int result = reverse(maxInt);
        System.out.println(result);
    }
}
