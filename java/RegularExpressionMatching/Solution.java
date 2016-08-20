package RegularExpressionMatching;

import java.util.*;

/**
 * Created by Luyz on 16/8/20.
 * https://leetcode.com/problems/regular-expression-matching/
 */
public class Solution {
    Map<String, Map<String, Boolean>> matchMap = new HashMap<>();
    public boolean isMatch(String s, String p) {
        return canMatch(s, p);
    }

    private boolean canMatch(String s, String p) {
        if (matchMap.containsKey(s) && matchMap.get(s).containsKey(p)){
            return matchMap.get(s).get(p);
        }
        Boolean result = false;
        if ("".equals(s) && "".equals(p)) {
            result = true;
        }
        else if("".equals(p) && !"".equals(s)){
            result = false;
        }
        else if ("".equals(s)){
            if (p.length() % 2 == 1){
                result = false;
            }
            else {
                result = true;
                for (int i = 1; i < p.length(); i += 2) {
                    if(p.charAt(i) != '*'){
                        result = false;
                        break;
                    }
                }
            }
        }
        else{
            if (p.length() >= 2 && p.charAt(1) == '*'){
                if (p.charAt(0) == '.'){
                    for (int i = 0; i < s.length() + 1; i++) {
                        result = result || canMatch(s.substring(i), p.substring(2));
                        if (result){
                            break;
                        }
                    }
                }
                else {
                    result = canMatch(s, p.substring(2));
                    int i = 0;
                    while(i < s.length() && s.charAt(i) == p.charAt(0) && !result){
                        result = result || canMatch(s.substring(i + 1), p.substring(2));
                        i += 1;
                    }
                }

            }
            else {
                if (p.charAt(0) == '.' || s.charAt(0) == p.charAt(0)){
                    result = canMatch(s.substring(1), p.substring(1));
                }
            }
        }

        if (!matchMap.containsKey(s)){
            matchMap.put(s, new HashMap<>());
        }
        matchMap.get(s).put(p, result);
        return result;
    }
}