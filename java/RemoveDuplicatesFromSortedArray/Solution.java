package RemoveDuplicatesFromSortedArray;

/**
 * Created by Luyz on 16/8/24.
 * https://leetcode.com/problems/remove-duplicates-from-sorted-array/
 */
public class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0){
            return 0;
        }
        int current = 0;
        int currentNum = nums[0];
        for (int i = 1; i < nums.length; i++) {
            int numI = nums[i];
            if (numI != currentNum){
                nums[++current] = numI;
                currentNum = numI;
            }
        }
        return current + 1;
    }
}