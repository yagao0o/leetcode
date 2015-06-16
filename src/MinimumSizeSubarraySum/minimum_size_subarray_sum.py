# Author  :  Yagao0o
# Date    :  2015-02-19
# Source  :  https://leetcode.com/problems/minimum-size-subarray-sum/

# Given an array of n positive integers and a positive integer s,
# find the minimal length of a subarray of which the sum >= s. If there isn't one, return 0 instead.
#
# For example, given the array [2,3,1,2,4,3] and s = 7,
# the subarray [4,3] has the minimal length under the problem constraint.
#
# Credits:
# Special thanks to @Freezen for adding this problem and creating all test cases.


class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        if not nums:
            return 0
        left = 0
        right = 0
        result = len(nums) + 1
        current_sum = nums[0]
        if current_sum > s:
            return 1
        while True:
            if current_sum < s:
                right += 1
                if right == len(nums):
                    break
                current_sum += nums[right]
                if current_sum >= s:
                    result = min(result, right - left + 1)
            else:
                current_sum -= nums[left]
                left += 1
                if current_sum >= s:
                    result = min(result, right - left + 1)
        return result if result <= len(nums) else 0