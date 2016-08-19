# Author  :  Yagao0o
# Date    :  2015-02-03
# Source  :  https://oj.leetcode.com/problems/4sum/

# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?
# Find all unique quadruplets in the array which gives the sum of target.
#
# Note:
# Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a <=b <= c <= d)
# The solution set must not contain duplicate quadruplets.
#     For example, given array S = {1 0 -1 0 -2 2}, and target = 0.
#
#     A solution set is:
#     (-1,  0, 0, 1)
#     (-2, -1, 1, 2)
#     (-2,  0, 0, 2)

class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        result = []
        num.sort()
        for i in range(len(num)):
            if i > 0 and num[i] == num[i - 1]:
                continue
            is_first = True
            for j in range(i + 1, len(num)):
                if not is_first and num[j] == num[j - 1]:
                    continue
                left = j + 1
                right = len(num) - 1
                while left < right:
                    summary = num[i] + num[j] + num[left] + num[right]
                    if summary == target:
                        result.append([num[i], num[j], num[left], num[right]])
                    if summary > target:
                        right -= 1
                        while num[right] == num[right + 1] and left < right:
                            right -= 1
                    else:
                        left += 1
                        while num[left] == num[left - 1] and left < right:
                            left += 1
                is_first = False
        return result

#Need to optimize.
#It's running too much time.
ll = [1, -2, -5, -4, -3, 3, 3, 5]
a = Solution()
print a.fourSum(ll, -11)