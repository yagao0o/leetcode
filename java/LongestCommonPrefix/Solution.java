package LongestCommonPrefix;

/**
 * Created by Luyz on 16/8/21.
 * https://leetcode.com/problems/longest-common-prefix/
 */

public class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0){
            return  "";
        }
        String result = strs[0];
        for (int i = 1; i < strs.length; i++) {
            result = getCommonPrefix(result, strs[i]);
        }
        return result;
    }

    private String getCommonPrefix(String str1, String str2){
        int length1 = str1.length();
        int length2 = str2.length();
        int minLength = length1<length2?length1:length2;
        for (int i = 0; i < minLength; i++) {
            if (str1.charAt(i) != str2.charAt(i)){
                return  str1.substring(0, i);
            }
        }
        return str1.substring(0, minLength);
    }
}