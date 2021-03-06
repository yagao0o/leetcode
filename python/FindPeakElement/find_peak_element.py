# Author  :  Yagao0o
# Date    :  2015-06-09
# Source  :  https://leetcode.com/problems/find-peak-element/

# A peak element is an element that is greater than its neighbors.
# Given an input array where num[i] <> num[i+1], find a peak element and return its index.
# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
# You may imagine that num[-1] = num[n] = -MAX_INT.
# For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
#
# Note:
# Your solution should be in logarithmic complexity.
#
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.

class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        elif nums[-1] > nums[-2]:
            return len(nums) - 1
        left = 0
        right = len(nums) - 1
        while left < right:
            middle = ( left + right ) / 2
            if nums[middle] > nums[middle - 1] :
                if nums[middle] > nums[middle + 1]:
                    return middle
                left = middle
            else:
                right = middle
        return left