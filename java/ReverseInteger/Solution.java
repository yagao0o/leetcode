package ReverseInteger;

/**
 * Created by Luyz on 16/8/20.
 * https://leetcode.com/problems/reverse-integer/
 */

public class Solution {
    public int reverse(int x) {
        boolean isNegative = x < 0;
        x = isNegative?-x:x;
        int result = 0;
        while (x > 0){
            // deal with
            if (result > 2147483647 / 10){
                return 0;
            }
            int newInt = x % 10;
            x = x / 10;
            result = result * 10 + newInt;
        }
        return isNegative?-result:result;
    }
}