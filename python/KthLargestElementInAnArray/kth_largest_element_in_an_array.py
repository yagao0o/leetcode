# Author  :  Yagao0o
# Date    :  2015/6/17
# Source  :  https://leetcode.com/problems/kth-largest-element-in-an-array/

# Find the kth largest element in an unsorted array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# For example,
# Given [3,2,1,5,6,4] and k = 2, return 5.
#
# Note:
# You may assume k is always valid, 1 ¡Ü k ¡Ü array's length.
#
# Credits:
# Special thanks to @mithmatt for adding this problem and creating all test cases.

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        nums.sort()
        return nums[-k]

    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest2(self, nums, k):
        self.merge_sort_k(nums, 0, len(nums) - 1, k)
        return nums[k - 1]

    def merge_sort_k(self, nums, start, end, k):
        if start == end:
            return
        middle = (start + end) / 2
        self.merge_sort_k(nums, start, middle, k)
        self.merge_sort_k(nums, middle + 1, end, k)
        #merge the former k or (end - start)
        left = nums[start: min(middle + 1,start + k)]
        left_flag = 0
        right_flag = middle + 1
        for i in range(min(end - start + 1, k)):
            if left[left_flag] > nums[right_flag]:
                nums[start + i] = left[left_flag]
                left_flag += 1
                if left_flag == len(left):
                    break
            else:
                nums[start + i] = nums[right_flag]
                right_flag += 1
                if right_flag > end:
                    for j in range(i + 1, min(end - start + 1, k)):
                        nums[start + j] = left[left_flag]
                        left_flag += 1
                    break