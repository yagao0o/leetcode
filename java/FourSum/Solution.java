package FourSum;

import java.util.ArrayList;
import java.util.List;

/**
 * 写的很复杂，考虑能不能更优雅一些
 */
class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        List<Integer> sortedArray = new ArrayList<>();
        for (int num : nums) {
            sortedArray.add(num);
        }
        sortedArray = quickSort(sortedArray);
        for (int i = 0; i < nums.length; i++) {
            nums[i] = sortedArray.get(i);
        }
        int totalLength = nums.length;
        List<List<Integer>> result = new ArrayList<>();
        int id1 = 0;
        while (id1 < nums.length - 3) {
            // ID1
            int min = nums[id1] + nums[id1 + 1] + nums[id1 + 2] + nums[id1 + 3];
            if (target < min) {
                break;
            } else if (target == min) {
                addToResult(result, nums[id1], nums[id1 + 1], nums[id1 + 2], nums[id1 + 3]);
                break;
            }
            int max = nums[id1] + nums[totalLength - 3] + nums[totalLength - 2] + nums[totalLength - 1];
            if (target == max) {
                addToResult(result, nums[id1], nums[totalLength - 3], nums[totalLength - 2], nums[totalLength - 1]);
            } else if (target < max) {
                int id2 = id1 + 1;
                while (id2 < nums.length - 2) {
                    min = nums[id1] + nums[id2] + nums[id2 + 1] + nums[id2 + 2];
                    if (target < min) {
                        break;
                    } else if (target == min) {
                        addToResult(result, nums[id1], nums[id2], nums[id2 + 1], nums[id2 + 2]);
                        break;
                    }
                    max = nums[id1] + nums[id2] + nums[totalLength - 2] + nums[totalLength - 1];
                    if (target == max) {
                        addToResult(result, nums[id1], nums[id2], nums[totalLength - 2], nums[totalLength - 1]);
                    } else if (target < max) {
                        int id3 = id2 + 1;
                        while (id3 < nums.length - 1) {
                            min = nums[id1] + nums[id2] + nums[id3] + nums[id3 + 1];
                            if (target < min) {
                                break;
                            } else if (target == min) {
                                addToResult(result, nums[id1], nums[id2], nums[id3], nums[id3 + 1]);
                                break;
                            }
                            max = nums[id1] + nums[id2] + nums[id3] + nums[totalLength - 1];
                            if (target == max) {
                                addToResult(result, nums[id1], nums[id2], nums[id3], nums[totalLength - 1]);
                            } else {
                                // 二分法查找id4
                                int left = id3 + 1, right = totalLength - 1;
                                while (left <= right){
                                    int middle = (left + right) / 2;
                                    int biggerOne = nums[middle];
                                    if (nums[id1] + nums[id2] + nums[id3] + nums[middle] == target){
                                        addToResult(result, nums[id1], nums[id2], nums[id3], nums[middle]);
                                        break;
                                    }
                                    else if (nums[id1] + nums[id2] + nums[id3] + nums[middle] < target){
                                        left = middle + 1;
                                    }
                                    else{
                                        right = middle - 1;
                                    }
                                }
                            }
                            id3 = findNextId(nums, id3);
                        }
                    }
                    id2 = findNextId(nums, id2);
                }
            }
            id1 = findNextId(nums, id1);
        }
        return result;
    }

    private int findNextId(int[] nums, int id) {
        int newId = id + 1;
        while (newId < nums.length) {
            if (nums[newId] != nums[id]) {
                break;
            }
            newId += 1;
        }
        return newId;
    }

    private void addToResult(List<List<Integer>> result, int n0, int n1, int n2, int n3) {
        List<Integer> newResult = new ArrayList<>();
        newResult.add(n0);
        newResult.add(n1);
        newResult.add(n2);
        newResult.add(n3);
        result.add(newResult);
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