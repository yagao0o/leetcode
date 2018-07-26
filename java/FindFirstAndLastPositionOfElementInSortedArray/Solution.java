package FindFirstAndLastPositionOfElementInSortedArray;

class Solution {
    public int[] searchRange(int[] nums, int target) {
        return searchRangeWithLeftAndRight(nums, 0, nums.length -1 , target);
    }

    public int[] searchRangeWithLeftAndRight(int[] nums, int left, int right, int target) {
        int[] result = new int[]{-1, -1};
        if (left > right || target < nums[left] || target > nums[right]) {
            return result;
        } else {
            int middle = (left + right) / 2;
            if (nums[middle] == target) {
                int[] leftResult = searchRangeWithLeftAndRight(nums, left, middle - 1, target);
                int[] rightResult = searchRangeWithLeftAndRight(nums, middle + 1, right, target);
                if (leftResult[0] == -1) {
                    result[0] = middle;
                } else {
                    result[0] = leftResult[0];
                }
                if (rightResult[1] == -1) {
                    result[1] = middle;
                } else {
                    result[1] = rightResult[1];
                }
            } else if (nums[middle] > target) {
                return searchRangeWithLeftAndRight(nums, left, middle - 1, target);
            } else  {
                return searchRangeWithLeftAndRight(nums, middle + 1, right, target);
            }
        }
        return result;
    }


    public static void main(String[] args) {
        Solution s = new Solution();
        int[] a = new int[]{5, 7, 7, 8, 8, 10};
        int[] x = s.searchRange(a, 8);
        System.out.println(x[0] + "," + x[1] );
        x = s.searchRange(a, 9);
        System.out.println(x[0] + "," + x[1] );
    }
}