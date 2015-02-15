# Author  :  Yagao0o
# Date    :  2015-02-15
# Source  :  https://oj.leetcode.com/problems/sort-colors/

# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
#
# For example,
# If n = 4 and k = 2, a solution is:
#
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        return self.get_combine(range(1, n + 1), k)

    def get_combine(self, numbers, k):
        result = []
        if k == 1:
            for number in numbers:
                result.append([number])
        else:
            for i in range(len(numbers)):
                number = numbers[i]
                for sub_result in self.get_combine(numbers[i + 1:], k - 1):
                    sub_result.insert(0, number)
                    result.append(sub_result)
        return result