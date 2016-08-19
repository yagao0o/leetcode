# Author  :  Yagao0o
# Date    :  2015/6/17
# Source  :  https://leetcode.com/problems/contains-duplicate-ii/
# Given an array of integers and an integer k,
# find out whether there there are two distinct indices i and j in the array
# such that nums[i] = nums[j] and the difference between i and j is at most k.


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        if k >= len(nums):
            num_set = set(nums)
            return not (len(num_set) == len(nums))
        nums_set = set([nums[i] for i in range(k + 1)])
        if len(nums_set) < k + 1:
            return True
        for i in range(k + 1, len(nums)):
            nums_set.remove(nums[i - k - 1])
            if nums[i] in nums_set:
                return True
            nums_set.add(nums[i])
        return False