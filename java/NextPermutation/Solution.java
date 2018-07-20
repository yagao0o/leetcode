package NextPermutation;

class Solution {
    public void nextPermutation(int[] nums) {
        if (nums.length <= 1) {
            return;
        }
        int maxReverseLength = 0;
        int i = nums[nums.length - 1];
        while (maxReverseLength < nums.length) {
            maxReverseLength += 1;
            if (nums[nums.length - maxReverseLength] < i) {
                maxReverseLength -= 1;
                break;
            }
            i = nums[nums.length - maxReverseLength];
        }
        if (maxReverseLength != nums.length) {
            int x = nums[nums.length - maxReverseLength - 1];
            int j = nums.length - 1;
            while (j > 0) {
                if(nums[j] > x){
                    nums[nums.length - maxReverseLength - 1] = nums[j];
                    nums[j] = x;
                    break;
                }
                j -= 1;
            }
        }
        int end = nums.length - 1;
        int start = nums.length - maxReverseLength;
        while (end >= start) {
            int tmp = nums[end];
            nums[end] = nums[start];
            nums[start] = tmp;
            end -= 1;
            start += 1;
        }
    }
}