package ImplementStrstr;

/**
 * Created by Luyz on 16/8/24.
 * https://leetcode.com/problems/implement-strstr/
 */
public class Solution {
    public int strStr(String haystack, String needle) {
        // Cheat method;
        // return haystack.indexOf(needle);
        int result = -1;
        if (needle.length() == 0){
            return 0;
        }
        int[] lastPos = new int[needle.length()];
        lastPos[0] = 0;
        for (int i = 1; i < needle.length(); i++) {
            if (needle.charAt(lastPos[i - 1]) == needle.charAt(i - 1)){
                if (lastPos[i - 1] + 1 != i)
                    lastPos[i] = lastPos[i - 1] + 1;
            }
        }
        int left = 0;
        int matchLength = 0;
        int maxLeft = haystack.length();
        while (left < maxLeft){
            char currentChar = haystack.charAt(left);
            if (currentChar == needle.charAt(matchLength)) {
                matchLength += 1;
            }
            else {
                while (matchLength != 0){
                    matchLength = lastPos[matchLength];
                    if (currentChar == needle.charAt(matchLength)){
                        matchLength += 1;
                        break;
                    }
                }
                if (matchLength == 0 && currentChar == needle.charAt(0)){
                    matchLength += 1;
                }
            }
            if (matchLength == needle.length()){
                result = left + 1 - matchLength;
                break;
            }
            left += 1;
        }
        return result;
    }
}