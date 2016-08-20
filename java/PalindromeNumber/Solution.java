package PalindromeNumber;

/**
 * Created by Luyz on 16/8/20.
 * https://leetcode.com/problems/palindrome-number/
 */
public class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0){
            return false;
        }
        int origin = x;
        int reverseInt = 0;
        while (origin > 0){
            reverseInt = reverseInt * 10 + origin % 10;
            origin = origin / 10;
        }
        return reverseInt == x;
    }
}