# Author  :  Yagao0o
# Date    :  2015-02-06
# Source  :  https://oj.leetcode.com/problems/combination-sum/

# Given a set of candidate numbers (C) and a target number (T),
# find all unique combinations in C where the candidate numbers sums to T.
#
# The same repeated number may be chosen from C unlimited number of times.
#
# Note:
# All numbers (including target) will be positive integers.
# Elements in a combination (a1, a2 ... ak) must be in non-descending order. (ie, a1 <= a2 ... <= ak).
# The solution set must not contain duplicate combinations.
# For example, given candidate set 2,3,6,7 and target 7,
# A solution set is:
# [7]
# [2, 2, 3]

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates.sort()
        return self.get_combination(candidates, target, 0)

    def get_combination(self, candidates, target, start):
        result = []
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                break
            elif candidates[i] == target:
                result.append([candidates[i]])
                break
            sub_results = self.get_combination(candidates, target - candidates[i], i)
            if sub_results:
                for sub_result in sub_results:
                    sub_result.insert(0, candidates[i])
                    result.append(sub_result)
        return result