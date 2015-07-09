# Author  :  Yagao0o
# Date    :  2015/7/9
# Source  :  https://leetcode.com/problems/summary-ranges/

# Given a sorted integer array without duplicates, return the summary of its ranges.
#
# For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
#
# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        if not nums:
            return []
        elif len(nums) == 1:
            return [str(nums[0])]
        left = 0
        right = len(nums) - 1
        return self.get_summary_range(nums, left, right)

    def get_summary_range(self, nums, left, right):
        if left == right:
            return [str(nums[left])]
        if nums[left] - nums[right] == left - right:
            return [str(nums[left]) + '->' + str(nums[right])]
        left_part = self.get_summary_range(nums, left, (left + right)  / 2)
        right_part = self.get_summary_range(nums, (left + right) / 2 + 1, right)
        if nums[(left + right) / 2] + 1 == nums[(left + right) / 2 + 1]:
            middle_part_begin = left_part[-1].split('-')[0] if left_part[-1].find('-') > 0 else left_part[-1]
            middle_part_end = right_part[0].split('>')[-1] if right_part[0].find('>') > 0 else right_part[0]
            return left_part[:-1] + [middle_part_begin + '->' + middle_part_end] + right_part[1:]
        else:
            return left_part + right_part

