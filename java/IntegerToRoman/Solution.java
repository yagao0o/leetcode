package IntegerToRoman;

import java.util.*;

/**
 * Created by Luyz on 16/8/21.
 * https://leetcode.com/problems/integer-to-roman/
 */
public class Solution {
    public String intToRoman(int num) {
        String result = "";
        int place4 = num / 1000;
        for (int i = 0; i < place4; i++) {
            result += "M";
        }
        result += lastIntToRoman(num / 100, "C" , "D", "M");
        result += lastIntToRoman(num / 10, "X", "L", "C");
        result += lastIntToRoman(num, "I", "V", "X");
        return result;
    }

    private String lastIntToRoman(int num, String one, String five, String ten){
        num = num % 10;
        if (num >= 5){
            if (num == 9){
                return one + ten;
            }
            else{
                String result = five;
                for (int i = 0; i < num - 5; i++) {
                    result += one;
                }
                return  result;
            }

        }
        else{
            if (num == 4){
                return one + five;
            }
            else{
                String result = "";
                for (int i = 0; i < num; i++) {
                    result += one;
                }
                return result;
            }
        }
    }
}
