package ThreeSum;

import java.util.*;

/**
 * Created by Luyz on 16/8/22.
 * https://leetcode.com/problems/3sum/
 */
public class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<Integer> sortedArray = new ArrayList<>();
        for (int num: nums){
            sortedArray.add(num);
        }
        sortedArray = quickSort(sortedArray);
        List<List<Integer>> result = new ArrayList<>();
        int i = 0;
        while (i < sortedArray.size()){
            int smallOne = sortedArray.get(i);
            int j = i + 1;
            while (j < sortedArray.size()){
                int middleOne = sortedArray.get(j);
                int target = 0 - smallOne - middleOne;
                int left = j + 1, right = sortedArray.size() - 1;
                while (left <= right){
                    int middle = (left + right) / 2;
                    int biggerOne = sortedArray.get(middle);
                    if (biggerOne == target){
                        List<Integer> newResult = new ArrayList<>();
                        newResult.add(smallOne);
                        newResult.add(middleOne);
                        newResult.add(biggerOne);
                        result.add(newResult);
                        break;
                    }
                    else if (biggerOne < target){
                        left = middle + 1;
                    }
                    else{
                        right = middle - 1;
                    }
                }
                while (j < sortedArray.size() && sortedArray.get(j) == middleOne){
                    j ++;
                }
            }
            while (i < sortedArray.size() && sortedArray.get(i) == smallOne){
                i ++;
            }
        }
        return result;
    }


    public List<Integer> quickSort(List<Integer> nums){
        if (nums.size() == 0){
            return new ArrayList<>();
        }
        else {
            List<Integer> smaller = new ArrayList<>();
            List<Integer> bigger = new ArrayList<>();
            Integer pivot = nums.get(0);
            for (int i = 1; i < nums.size(); i++) {
                Integer currentNum = nums.get(i);
                if (currentNum < pivot){
                    smaller.add(currentNum);
                }
                else {
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