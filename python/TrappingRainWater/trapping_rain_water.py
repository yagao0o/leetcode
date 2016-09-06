# coding: UTF8
# Author  :  Yagao0o
# Date    :  16/9/6
# Description  :  https://leetcode.com/problems/trapping-rain-water/

#
# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it is able to trap after raining.
#
# For example,
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        return self.count(height, 0, len(height) - 1)

    def count(self, heights, left, right):
        if left + 1 >= right:
            return 0
        middle_left = left + 1
        middle_right = right - 1
        while middle_left < middle_right:
            if heights[middle_left] < heights[middle_right]:
                middle_left += 1
            else:
                middle_right -= 1
        if heights[left] > heights[middle_left] and heights[right] > heights[middle_left]:
            top = heights[left] if heights[left] < heights[right] else heights[right]
            result = 0
            for i in xrange(left + 1, right):
                result += top - heights[i]
            return result
        else:
            left_part = self.count(heights, left, middle_left)
            right_part = self.count(heights, middle_left, right)
            return left_part + right_part
