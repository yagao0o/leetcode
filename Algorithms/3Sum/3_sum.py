# Author  :  Yagao0o
# Date    :  2015-01-29
# Source  :  https://oj.leetcode.com/problems/3sum/

# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.
#
# Note:
# Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <= c)
# The solution set must not contain duplicate triplets.
#     For example, given array S = {-1 0 1 2 -1 -4},
#
#     A solution set is:
#     (-1, 0, 1)
#     (-1, -1, 2)

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        result = []
        num.sort()
        last = 1
        for i in range(len(num)):
            if last == num[i]:
                continue
            elif num[i] > 0:
                break
            last = num[i]
            left = i + 1
            right = len(num) - 1
            while left < right:
                summary = num[i] + num[left] + num[right]
                if summary == 0:
                    result.append([num[i], num[left], num[right]])
                    left += 1
                    while num[left] == num[left - 1] and left < right:
                        left += 1
                elif summary > 0:
                    right -= 1
                    while num[right] == num[right + 1] and left < right:
                        right -= 1
                else:
                    left += 1
                    while num[left] == num[left - 1] and left < right:
                        left += 1
        return result