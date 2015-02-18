# Author  :  Yagao0o
# Date    :  2015-02-
# Source  :  https://oj.leetcode.com/problems/subsets-ii/

# Given a collection of integers that might contain duplicates, S, return all possible subsets.
#
# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# For example,
# If S = [1,2,2], a solution is:
#
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        S.sort()
        group_set = []
        current_group = []
        current = None
        current_times = 0
        for i in range(len(S)):
            if S[i] != current:
                current = S[i]
                current_times = 1
                if current_group:
                    group_set.append(current_group)
                current_group = [[current]]
            else:
                current_times += 1
                current_group.append([current]*current_times)
        if current_group:
            group_set.append(current_group)
        result = self.get_subsets(group_set)
        return result

    def get_subsets(self, group_set):
        if len(group_set) == 1:
            return group_set[0] + [[]]
        current_group = group_set.pop(0)
        sub_results = self.get_subsets(group_set)
        result = []
        for sub_result in sub_results:
            result.append(sub_result)
            for current_set in current_group:
                result.append(current_set + sub_result)
        return result


a = Solution()
print a.subsetsWithDup([1,2,2])