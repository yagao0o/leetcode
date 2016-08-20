package LongestPalindromicSubstring;

/**
 * Created by Luyz on 16/8/20.
 * https://leetcode.com/problems/longest-palindromic-substring/
 */
public class Solution {
    public String longestPalindrome(String s) {
        int longestStart = 0;
        int longestEnd = 1;
        boolean oddFaild = false;
        boolean evenFaild = false;
        if ("".equals(s)){
            return "";
        }
        int length = s.length();
        boolean[] odd = new boolean[length];
        boolean[] even = new boolean[length];
        for (int i = 0; i < length; i++) {
            odd[i] = true;
            even[i] = true;
        }
        for (int j = 1; j < length;j++) {
            if (j % 2 == 0 && !oddFaild){
                oddFaild = true;
                //use odd
                for (int i = 0; i < length - j; i++) {
                    odd[i] = odd[i + 1] && s.charAt(i) == s.charAt(i + j);
                    if (oddFaild && odd[i]){
                        oddFaild = false;
                        longestStart = i;
                        longestEnd = i + j + 1;
                    }
                }
            }
            else if (j % 2 == 1 && !evenFaild){
                evenFaild = true;
                for (int i = 0; i < length - j; i++) {
                    even[i] = even[i + 1] && s.charAt(i) == s.charAt(i + j);
                    if (evenFaild && even[i]){
                        evenFaild = false;
                        longestStart = i;
                        longestEnd = i + j + 1;
                    }
                }
            }
            if(oddFaild && evenFaild)
                break;
        }
        return s.substring(longestStart, longestEnd);
    }
}