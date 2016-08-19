# Author  :  Yagao0o
# Date    :  2015-02-10
# Source  :  https://oj.leetcode.com/problems/permutations/

# Given a collection of numbers, return all possible permutations.
#
# For example,
# [1,2,3] have the following permutations:
# [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        num.sort()
        return self.get_permute(num)

    def get_permute(self, num):
        if len(num) == 1:
            return [[num[0]]]
        result = []
        last = None
        for i in range(len(num)):
            if num[i] == last:
                continue
            last = num[i]
            current = num.pop(i)
            for sub_result in self.permute(num):
                sub_result.append(current)
                result.append(sub_result)
            num.insert(i, current)
        return result