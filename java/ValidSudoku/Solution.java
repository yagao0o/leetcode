package ValidSudoku;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

class Solution {
    public Map<Character, Integer> getMap() {
        Map<Character, Integer> map = new HashMap<>();
        map.put('.', 0);
        for (int i = 1; i < 10; i++) {
            char c = (char) ('1' + i - 1);
            map.put(c, i);
        }
        return map;
    }

    public boolean isValidSudoku(char[][] board) {
        Map<Character, Integer> map = getMap();
        for (int i = 0; i < 9; i++) {
            boolean[] checker = new boolean[10];
            // 行
            for (int j = 0; j < 9; j++) {
                int num = map.get(board[i][j]);
                if (num != 0 && checker[num]) {
                    return false;
                }
                checker[num] = true;
            }
            checker = new boolean[10];
            // 列
            for (int j = 0; j < 9; j++) {
                int num = map.get(board[j][i]);
                if (num != 0 && checker[num]) {
                    return false;
                }
                checker[num] = true;
            }
            checker = new boolean[10];
            // 宫
            for (int j = 0; j < 9; j++) {
                int num = map.get(board[i / 3 * 3 + j / 3][i % 3 * 3 + j % 3]);
                if (num != 0 && checker[num]) {
                    return false;
                }
                checker[num] = true;
            }
        }
        return true;
    }

    public boolean isValidSudoku2(char[][] board) {
        Set<Character> rSet = new HashSet<>();
        Set<Character> cSet = new HashSet<>();
        Set<Character> sSet = new HashSet<>();
        for (int i = 0; i < 9; i++) {
            boolean[] checker = new boolean[10];
            // 行
            for (int j = 0; j < 9; j++) {
                char l = board[i][j];
                if (l != '.' && rSet.contains(l)){
                    return false;
                }
                rSet.add(l);

                l = board[j][i];
                if (l != '.' && cSet.contains(l)){
                    return false;
                }
                cSet.add(l);

                l = board[i / 3 * 3 + j / 3][i % 3 * 3 + j % 3];

                if (l != '.' && sSet.contains(l)){
                    return false;
                }
                sSet.add(l);
            }
            rSet.clear();
            cSet.clear();
            sSet.clear();
        }
        return true;
    }
}
