# Author  :  Yagao0o
# Date    :  2015-02-02
# Source  :  https://oj.leetcode.com/problems/3sum-closest/

# Given an array S of n integers, find three integers in S such that the sum is closest to a given number,
# target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
#     For example, given array S = {-1 2 1 -4}, and target = 1.
#
#     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        if len(num) == 3:
            return num[0] + num[1] + num[2]
        num.sort()
        result = num[0] + num[1] + num[2]
        for i in range(len(num)):
            left = i + 1
            right = len(num) - 1
            while left < right:
                current = num[i] + num[left] + num[right]
                if current == target:
                    return target
                elif abs(current - target) < abs(result - target):
                    result = current
                if current > target:
                    right -= 1
                else:
                    left += 1
        return result