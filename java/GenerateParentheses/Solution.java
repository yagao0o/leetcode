package GenerateParentheses;
import java.util.*;
/**
 * Created by Luyz on 16/8/23.
 * https://leetcode.com/problems/generate-parentheses/
 */
public class Solution {
    public List<String> generateParenthesis(int n) {
        return generate("", n, 0);
    }

    public List<String> generate(String currentState,int leftRemain,int rightRemain){
        List<String> result = new ArrayList<>();
        if (leftRemain == 0){
            if (rightRemain != 0) {
                return generate(currentState + ")", 0, rightRemain - 1);
            }
            else {
                result.add(currentState);
            }
        }
        else {
            result = generate(currentState + "(", leftRemain - 1, rightRemain + 1);
            if (rightRemain > 0){
                result.addAll(generate(currentState + ")", leftRemain, rightRemain - 1));
            }
        }
        return result;
    }
}
