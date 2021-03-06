# Author  :  Yagao0o
# Date    :  2015/6/17
# Source  :  https://leetcode.com/problems/combination-sum-iii/

# Find all possible combinations of k numbers that add up to a number n,
# given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
#
# Ensure that numbers within the set are sorted in ascending order.
#
# Example 1:#
# Input: k = 3, n = 7#
# Output: [[1,2,4]]
#
# Example 2:
# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]
# Credits:
# Special thanks to @mithmatt for adding this problem and creating all test cases.

class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        nums = range(1,10)
        return self.get_combination(nums, n, 0, k)

    def get_combination(self, nums, target, start, remain):
        result = []
        if remain == 0:
            return result
        for i in range(start, len(nums)):
            if nums[i] > target:
                break
            elif nums[i] == target and remain == 1:
                result.append([nums[i]])
                break
            sub_results = self.get_combination(nums, target - nums[i], i + 1, remain - 1)
            if sub_results:
                for sub_result in sub_results:
                    sub_result.insert(0, nums[i])
                    result.append(sub_result)
        return result