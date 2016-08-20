package StringToInteger;

/**
 * Created by Luyz on 16/8/20.
 * https://leetcode.com/submissions/detail/71007723/
 */
public class Solution {
    public int myAtoi(String str) {
        str = str.trim();
        if (str.equals("")){
            return 0;
        }
        boolean isNegative = '-' == str.charAt(0);
        int result = 0;
        int start = isNegative?1:0;
        if ('+' == str.charAt(0)){
            start = 1;
        }
        for (int i = start; i < str.length(); i++) {
            int newInt = str.charAt(i) - '0';
            if (newInt >= 0 && newInt <=9) {
                int newResult = result * 10 + newInt;
                if (newResult / 10 != result){
                    return isNegative?-2147483648:2147483647;
                }
                result = newResult;
            }
            else {
                break;
            }
        }
        return isNegative?-result:result;
    }
}
