package RomanToInteger;

import java.util.*;

/**
 * Created by Luyz on 16/8/21.
 * https://leetcode.com/problems/roman-to-integer/
 */

public class Solution {
    public int romanToInt(String s) {
        Map<Character, Integer> map = new HashMap<>();
        map.put('M', 1000);
        map.put('D', 500);
        map.put('C', 100);
        map.put('L', 50);
        map.put('X', 10);
        map.put('V', 5);
        map.put('I', 1);
        int result = 0;
        int last = 0;
        for (int i = 0; i < s.length(); i++) {
            int newNum = map.get(s.charAt(i));
            if (last < newNum) {
                last = newNum - last;
            }
            else {
                result += last;
                last = newNum;
            }
        }
        return result + last;
    }
}