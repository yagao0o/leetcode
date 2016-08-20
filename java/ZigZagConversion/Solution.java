package ZigZagConversion;

import java.util.*;

/**
 * Created by Luyz on 16/8/20.
 * https://leetcode.com/problems/zigzag-conversion/
 */

public class Solution {
    public String convert(String s, int numRows) {
        if (numRows == 1){
            return s;
        }
        String[] stringList = new String[numRows];
        for (int i = 0; i < numRows; i++) {
            stringList[i] = "";
        }
        for (int i = 0; i < s.length(); i++) {
            int x = i % (2* numRows - 2);
            if (x > numRows - 1){
                x = 2 * numRows - 2 - x;
            }
            stringList[x] += s.charAt(i);
        }
        String result = "";
        for (int i = 0; i < numRows; i++) {
            result += stringList[i];
        }
        return result;
    }
}
