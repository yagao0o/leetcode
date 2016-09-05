# coding: UTF8
# Author  :  Yagao0o
# Date    :  16/9/5
# Description  :  https://leetcode.com/problems/first-missing-positive/

# Given an unsorted integer array, find the first missing positive integer.
#
# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.
#
# Your algorithm should run in O(n) time and uses constant space.


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pass
        has = [False]*len(nums)

        for i in nums:
            if 0 < i <= len(nums):
                has[i - 1] = True
        for i in xrange(len(has)):
            if not has[i]:
                return i + 1
        return len(nums) + 1
