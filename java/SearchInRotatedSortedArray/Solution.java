package SearchInRotatedSortedArray;

class Solution {
    public int search(int[] nums, int target) {
        if (nums.length == 0) {
            return -1;
        }
        return searchRotated(nums, 0, nums.length - 1, target);
    }

    public int searchRotated(int[] nums, int left, int right, int target) {
        if (left > right) {
            return -1;
        }
        if (left == right) {
            if (nums[left] == target) {
                return left;
            }
        } else {
            int mid = (left + right) / 2;
            if (nums[mid] == target) {
                return mid;
            }
            if (nums[mid] >= nums[left]) {
                // 左边正序
                if (target >= nums[left] && target < nums[mid]) {
                    return searchNormal(nums, left, mid - 1, target);
                } else {
                    return searchRotated(nums, mid + 1, right, target);
                }
            } else {
                // 右边正序
                if (target > nums[mid] && target <= nums[right]) {
                    return searchNormal(nums, mid + 1, right, target);
                } else {
                    return searchRotated(nums, left, mid - 1, target);
                }
            }
        }
        return -1;
    }

    public int searchNormal(int[] nums, int left, int right, int target) {
        if (left == right) {
            if (nums[left] == target) {
                return left;
            }
        } else {
            while (left <= right) {
                int mid = (left + right) / 2;
                if (nums[mid] == target) {
                    return mid;
                } else if (nums[mid] < target) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }
        return -1;
    }
}