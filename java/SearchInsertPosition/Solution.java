package SearchInsertPosition;

class Solution {
    public static int searchInsert(int[] nums, int target) {
        if (nums.length == 0 || target <= nums[0]) {
            return 0;
        } else if (target > nums[nums.length - 1]) {
            return nums.length;
        } else if (target == nums[nums.length - 1]) {
            return nums.length - 1;
        }
        int left = 0;
        int right = nums.length;
        while (left != right) {
            if (right - left == 1) {
                return right;
            }
            int middle = (left + right) / 2;
            if (nums[middle] == target) {
                return middle;
            } else if (nums[middle] > target) {
                right = middle;
            } else {
                left = middle;
            }
        }
        return left;
    }
}
