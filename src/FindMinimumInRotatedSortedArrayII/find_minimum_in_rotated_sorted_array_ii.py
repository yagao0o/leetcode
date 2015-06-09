# Author  :  Yagao0o
# Date    :  2015-06-09
# Source  :  https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

# Follow up for "Find Minimum in Rotated Sorted Array":
# What if duplicates are allowed?
#
# Would this affect the run-time complexity? How and why?
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# Find the minimum element.
#
# The array may contain duplicates.

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]
        for i in range(1,len(nums)):
            if nums[i] < nums[i - 1]:
                return nums[i]
        return nums[0]