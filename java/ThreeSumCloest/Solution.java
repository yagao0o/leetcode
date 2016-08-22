package ThreeSumCloest;

import java.util.*;

/**
 * Created by Luyz on 16/8/22.
 * https://leetcode.com/problems/3sum-closest/
 */
public class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int cloest = nums[0] + nums[1] + nums[2];
        int distance = cloest > target? cloest - target:target - cloest;
        int i = 0;
        while (i < nums.length - 2 && distance > 0){
            int smallerOne = nums[i];
            int j = i + 1;
            while (j < nums.length - 1 && distance > 0){
                int middleOne = nums[j];
                int expect = target - smallerOne - middleOne;
                int left = j + 1;
                int right = nums.length - 1;
                while (left < right){
                    int middle = (left + right) / 2;
                    int laggerOne = nums[middle];
                    if (laggerOne == expect){
                        return target;
                    }
                    else if (laggerOne > expect){
                        right = middle - 1;
                    }
                    else {
                        left = middle + 1;
                    }
                }
                int thisSum = smallerOne + middleOne + nums[left];
                int thisDistance = thisSum > target?thisSum - target:target - thisSum;
                if (thisDistance < distance){
                    cloest = thisSum;
                    distance = thisDistance;
                }
                while (j < nums.length - 1 && nums[j] == middleOne) j++;
            }
            while (i < nums.length - 2 && nums[i] == smallerOne) i++;
        }
        return cloest;
    }
}