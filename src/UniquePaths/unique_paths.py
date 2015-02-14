# Author  :  Yagao0o
# Date    :  2015-02-14
# Source  :  https://oj.leetcode.com/problems/unique-paths/

# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#
# How many possible unique paths are there?

#result = C(m + n - 2, m - 1) = (m + n - 2)! / ( (m - 1)! * (n - 1)! )

class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        numerator = 1
        denominator = 1
        for i in range(1,min(m, n)):
            numerator *= m + n - 1 - i
            denominator *= i
        return numerator / denominator