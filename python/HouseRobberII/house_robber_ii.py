# Author  :  Yagao0o
# Date    :  2015/6/17
# Source  :  https://leetcode.com/problems/house-robber-ii/

# Note: This is an extension of House Robber.
#
# After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.
#
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
#
# Credits:
# Special thanks to @Freezen for adding this problem and creating all test cases.

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if not nums:
            return 0
        left = nums[0]
        right = nums[0]
        for i in range(2,len(nums) - 1):
            left, right = right, max(right, left + nums[i])
        result_with_first = right
        left = 0
        right= 0
        for i in range(1,len(nums)):
            left, right = right, max(right,left + nums[i])
        return max(result_with_first,right)