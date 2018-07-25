package FourSum;

import java.util.*;

public class Solution2 {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        List<Integer> sortedArray = new ArrayList<>();
        for (int num : nums) {
            sortedArray.add(num);
        }
        sortedArray = quickSort(sortedArray);

        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < sortedArray.size(); i++) {
            if (i > 0 && sortedArray.get(i).intValue() == sortedArray.get(i - 1).intValue()) {
                continue;
            }
            List<Integer> subArr = copyFrom(sortedArray, i);
            List<List<Integer>> threeSum = threeSum(subArr, target - sortedArray.get(i));
            for (List<Integer> arr : threeSum) {
                arr.add(0, sortedArray.get(i));
                result.add(arr);
            }
        }
        return result;
    }

    private List<Integer> copyFrom(List<Integer> sortedArray, int i) {

        List<Integer> result = new ArrayList<>();
        for (int j = i + 1; j < sortedArray.size(); j++) {
            result.add(sortedArray.get(j));
        }
        return result;
    }

    private List<List<Integer>> threeSum(List<Integer> sortedArray, int tar) {
        List<List<Integer>> result = new ArrayList<>();
        int i = 0;
        while (i < sortedArray.size()) {
            int smallOne = sortedArray.get(i);
            int j = i + 1;
            while (j < sortedArray.size()) {
                int middleOne = sortedArray.get(j);
                int target = tar - smallOne - middleOne;
                int left = j + 1, right = sortedArray.size() - 1;
                while (left <= right) {
                    int middle = (left + right) / 2;
                    int biggerOne = sortedArray.get(middle);
                    if (biggerOne == target) {
                        List<Integer> newResult = new ArrayList<>();
                        newResult.add(smallOne);
                        newResult.add(middleOne);
                        newResult.add(biggerOne);
                        result.add(newResult);
                        break;
                    } else if (biggerOne < target) {
                        left = middle + 1;
                    } else {
                        right = middle - 1;
                    }
                }
                while (j < sortedArray.size() && sortedArray.get(j) == middleOne) {
                    j++;
                }
            }
            while (i < sortedArray.size() && sortedArray.get(i) == smallOne) {
                i++;
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


    private void showList(List<Integer> sortedArray) {
        for (int i = 0; i < sortedArray.size(); i++) {
            System.out.print(sortedArray.get(i) + ",");
        }
    }

    public static void main(String[] args) {
        Solution2 s = new Solution2();
        List<List<Integer>> t = s.fourSum(new int[]{-497, -494, -484, -477, -453, -453, -444, -442, -428, -420, -401, -393, -392, -381, -357, -357, -327, -323, -306, -285, -284, -263, -262, -254, -243, -234, -208, -170, -166, -162, -158, -136, -133, -130, -119, -114, -101, -100, -86, -66, -65, -6, 1, 3, 4, 11, 69, 77, 78, 107, 108, 108, 121, 123, 136, 137, 151, 153, 155, 166, 170, 175, 179, 211, 230, 251, 255, 266, 288, 306, 308, 310, 314, 321, 322, 331, 333, 334, 347, 349, 356, 357, 360, 361, 361, 367, 375, 378, 387, 387, 408, 414, 421, 435, 439, 440, 441, 470, 492}, 1682);
        for (int i = 0; i < t.size(); i++) {
            System.out.println(i + ":");
            s.showList(t.get(i));
            System.out.println();
        }
    }
}
