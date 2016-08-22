package LetterCombinationsOfPhoneNumber;

import java.util.*;
/**
 * Created by Luyz on 16/8/23.
 * https://leetcode.com/problems/letter-combinations-of-a-phone-number/
 */
public class Solution {
    public List<String> letterCombinations(String digits) {
        if ("".equals(digits)){
            return new ArrayList<>();
        }
        HashMap<Character, String[]> keyMap = new HashMap<>();
        keyMap.put('0', new String[]{" "});
        keyMap.put('2', new String[]{"a","b","c"});
        keyMap.put('3', new String[]{"d","e","f"});
        keyMap.put('4', new String[]{"g","h","i"});
        keyMap.put('5', new String[]{"j","k","l"});
        keyMap.put('6', new String[]{"m","n","o"});
        keyMap.put('7', new String[]{"p","q","r","s"});
        keyMap.put('8', new String[]{"t","u","v"});
        keyMap.put('9', new String[]{"w","x","y","z"});
        keyMap.put('1', new String[]{""});
        ArrayList<String> result = new ArrayList<>();
        result.add("");
        for (int i = 0; i < digits.length(); i++) {
            ArrayList<String> newResult = new ArrayList<>();
            char c = digits.charAt(i);
            for (String s: keyMap.get(c)){
                for (String s2: result){
                    newResult.add(s2 + s);
                }
            }
            result = newResult;
        }
        return result;
    }
}
