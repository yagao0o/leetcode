# Author  :  Yagao0o
# Date    :  2015-01-27
# Source  :  https://oj.leetcode.com/problems/container-with-most-water/

# Given n non-negative integers a1, a2, ..., an,  where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container.

class Solution:
    # @return an integer
    def maxArea(self, height):
        max_container = 0
        left = 0
        current_left_height = height[left]
        right = len(height) - 1
        current_right_height = height[right]
        while left < right:
            current_container = (right - left) * min(height[left], height[right])
            if current_container > max_container:
                max_container = current_container
            #count
            if current_left_height < current_right_height:
                while height[left] <= current_left_height and left < right:
                    left += 1
                current_left_height = height[left]
            else:
                while height[right] <= current_right_height and right > left:
                    right -= 1
                current_right_height = height[right]
        return max_container

# if ai and aj ( i < j ) contains the max container
# to all  n < i  ,we have  an < ai
# to all  N > j  , we have aN < aj
# result = (j - i) * min(ai, aj)
# we could set a flag at each side
# and raise flag up on each side one by one
# and get to the top finally
