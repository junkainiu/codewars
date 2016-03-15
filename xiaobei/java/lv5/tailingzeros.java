import java.math.BigDecimal;

public class Solution {
    private static BigDecimal factorial(BigDecimal n) {
        BigDecimal bigDecimal = new BigDecimal(1);
        if (n.equals(bigDecimal)) {
            return bigDecimal;
        } else {
            return n.multiply(factorial(n.subtract(bigDecimal)));
        }
    }

    private static int countZero(BigDecimal n) {
        BigDecimal bd1 = new BigDecimal(10);
        BigDecimal bd2 = new BigDecimal(0);
        int count = 0;
        while (n.divideAndRemainder(bd1)[1].equals(bd2)) {
            n = n.divideAndRemainder(bd1)[0];
            count++;
        }
        return count;
    }

    public static int zeros(int num) {
        BigDecimal bigDecimal = new BigDecimal(num);
        BigDecimal val = factorial(bigDecimal);
        int result = countZero(val);
        return result;
    }
}
