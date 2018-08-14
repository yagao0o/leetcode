package CombinationSum;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        if (candidates.length == 0){
            return result;
        }
        List<Integer> sortedList = new ArrayList<>();
        for (int i = 0; i < candidates.length; i++) {
            sortedList.add(candidates[i]);
        }
        sortedList = quickSort(sortedList);
        for (int i = 0; i < candidates.length; i++) {
            candidates[i] = sortedList.get(i);
        }

        Stack<Integer> stack = new Stack<>();
        int totalLength = candidates.length;

        stack.push(0);
        int currentSum = candidates[0];
        while (true) {
            // 计算是否相等
            if (currentSum < target) {
                //     小于则添加一个数
                int i = stack.peek();
                currentSum += candidates[i];
                stack.push(i);
            }
            else{
                if (currentSum == target) {
                    //     合适则添加到result
                    List<Integer> newResult = new ArrayList<>();
                    for (int i = 0; i < stack.size(); i++) {
                        newResult.add(candidates[stack.get(i)]);
                    }
                    result.add(newResult);
                }
                //删除当前数，最后一个数 + 1,(若+1后超出，则重复执行本步） (大于或等于时）
                int last = stack.pop();
                currentSum -= candidates[last];
                while (!stack.isEmpty()) {
                    last = stack.pop();
                    currentSum -= candidates[last];
                    last += 1;
                    if (last < totalLength){
                        stack.push(last);
                        currentSum += candidates[last];
                        break;
                    }
                }
                if (stack.isEmpty()) {
                    break;
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
