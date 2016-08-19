package LongestSubstringWithoutRepeatingCharacters;


import java.util.HashMap;
import java.util.Map;

/**
 * Created by Luyz on 16/8/19.
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/
 */

public class Solution {
    public int lengthOfLongestSubstring(String s) {
        int longest = 0;
        int head = -1;
        int tail = 0;
        Map<Character,Integer> charMap = new HashMap<>();
        while (tail < s.length()){
            Character c = s.charAt(tail);
            if (charMap.containsKey(c)) {
                for (int i = head + 1; i < charMap.get(c); i++) {
                    charMap.remove(s.charAt(i));
                }
                head = charMap.put(c, tail);
            }
            else {
                charMap.put(c, tail);
                longest = tail - head > longest?tail - head:longest;
            }
            tail += 1;
        }
        return longest;
    }
}