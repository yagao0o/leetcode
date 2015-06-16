# Author  :  Yagao0o
# Date    :  2015-02-15
# Source  :  https://oj.leetcode.com/problems/subsets/

# Given a set of distinct integers, S, return all possible subsets.
#
# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# For example,
# If S = [1,2,3], a solution is:
#
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]


class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        S.sort()
        return self.get_subsets(S)

    def get_subsets(self, S):
        if len(S) == 1:
            return [[], [S[0]]]
        number = S.pop(0)
        result = []
        for sub_result in self.subsets(S):
            result.append(sub_result[:])
            sub_result.insert(0, number)
            result.append(sub_result)
        return result