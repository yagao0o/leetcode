# coding: UTF8
# Author  :  Yagao0o
# Date    :  16/9/1
# Description  :  https://leetcode.com/problems/search-in-rotated-sorted-array/

# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.search_in_rotated_array(nums, 0, len(nums) - 1, target)

    def search_in_rotated_array(self, nums, left, right, target):
        result = -1
        if nums[left] <= nums[right]:
            return self.search_in_sorted_array(nums, left, right, target)
        else:
            if nums[left] > target > nums[right]:
                return -1
            while left <= right:
                isBigger = target >= nums[left]
                middle = (left + right) / 2
                mid_num = nums[middle]
                if mid_num == target:
                    return middle
                if mid_num >= nums[left]:
                    if isBigger and target < mid_num:
                        return self.search_in_sorted_array(nums, left, middle - 1, target)
                    else:
                        left = middle + 1
                else:
                    if not isBigger and target > mid_num:
                        return self.search_in_sorted_array(nums, middle + 1, right, target)
                    else:
                        right = middle - 1
        return result

    def search_in_sorted_array(self, nums, left, right, target):
        while left <= right:
            middle = (left + right) / 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        return -1
