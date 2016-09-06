# coding: UTF8
# Author  :  Yagao0o
# Date    :  16/9/6
# Description  :  https://leetcode.com/problems/jump-game-ii/

# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Your goal is to reach the last index in the minimum number of jumps.
#
# For example:
# Given array A = [2,3,1,1,4]
#
# The minimum number of jumps to reach the last index is 2.
# (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
#
# Note:
# You can assume that you can always reach the last index.


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        steps = 0
        i = 0
        next_max = 0
        current_max = 0
        while i < len(nums):
            while i <= current_max:
                if i == len(nums) - 1:
                    return steps
                next_max = next_max if next_max > i + nums[i] else i + nums[i]
                i += 1
            steps += 1
            current_max = next_max
