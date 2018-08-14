package CombinationSum;

import java.util.*;
import java.util.stream.Collectors;

class Solution2 {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<Integer> sortedList = new ArrayList<>();
        for (int i = 0; i < candidates.length; i++) {
            sortedList.add(candidates[i]);
        }
        sortedList = quickSort(sortedList);
        for (int i = 0; i < candidates.length; i++) {
            candidates[i] = sortedList.get(i);
        }

        return getSum(candidates, 0, target);
    }

    public List<List<Integer>> getSum(int[] candidates, int start, int target) {
        List<List<Integer>> result = new ArrayList<>();
        if (start < candidates.length) {
            if (candidates[start] <= target) {
                if (candidates[start] == target) {
                    List<Integer> available = new ArrayList<>();
                    available.add(target);
                    result.add(available);
                }
                else {
                    for (int i = start; i < candidates.length; i++) {
                        if (candidates[i] == target){
                            List<Integer> available = new ArrayList<>();
                            available.add(candidates[i]);
                            result.add(available);
                            break;
                        }
                        else if (candidates[i] * 2 > target){
                            continue;
                        }
                        int newTarget = target - candidates[i];
                        for (List<Integer> ls: getSum(candidates, i, newTarget)) {
                            if (ls.get(0) < candidates[i]){
                                continue;
                            }
                            List<Integer> newLs = ls.stream().collect(Collectors.toList());
                            newLs.add(0, candidates[i]);
                            result.add(newLs);
                        }
                    }
                }
            }
        }
        return result;
    }


    private List<Integer> quickSort(List<Integer> nums) {
        if (nums.size() == 0) {
            return new ArrayList<>();
        } else {
            List<Integer> smaller = new ArrayList<>();
            List<Integer> bigger = new ArrayList<>();
            Integer pivot = nums.get(0);
            for (int i = 1; i < nums.size(); i++) {
                Integer currentNum = nums.get(i);
                if (currentNum < pivot) {
                    smaller.add(currentNum);
                } else {
                    bigger.add(currentNum);
                }
            }
            smaller = quickSort(smaller);
            bigger = quickSort(bigger);
            smaller.add(pivot);
            smaller.addAll(bigger);
            return smaller;
        }
    }
}
