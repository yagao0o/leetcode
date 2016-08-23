package ValidParentheses;

/**
 * Created by Luyz on 16/8/23.
 * https://leetcode.com/problems/valid-parentheses/
 */
public class Solution {
    public boolean isValid(String s) {
        char[] parenthesesStack = new char[s.length()];
        int stackSize = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(' || c =='[' || c == '{') {
                parenthesesStack[stackSize++] = c;
            }
            else if (c == ')' && (stackSize == 0 || parenthesesStack[--stackSize] != '(')){
                return false;
            }
            else if (c == ']' && (stackSize == 0 || parenthesesStack[--stackSize] != '[')){
                return false;
            }
            else if (c == '}' && (stackSize == 0 || parenthesesStack[--stackSize] != '{')){
                return false;
            }
        }
        return stackSize == 0;
    }
}
