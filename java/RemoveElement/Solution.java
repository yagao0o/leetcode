package RemoveElement;

/**
 * Created by Luyz on 16/8/24.
 * https://leetcode.com/problems/remove-element/
 */

public class Solution {
    public int removeElement(int[] nums, int val) {
        if (nums.length == 0){
            return 0;
        }
        int left = 0;
        int right = nums.length - 1;
        while (left <= right){
            while (left < nums.length && nums[left] != val){
                left += 1;
            }
            while (right >= left && nums[right] == val){
                right -= 1;
            }
            if (left < nums.length && right > left){
                nums[left] = nums[right];
                nums[right] = val;
                left += 1;
                right -= 1;
            }
        }
        return left;
    }
}