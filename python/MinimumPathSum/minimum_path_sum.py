# Author  :  Yagao0o
# Date    :  2015-02-14
# Source  :  https://oj.leetcode.com/problems/minimum-path-sum/

# Given a m x n grid filled with non-negative numbers,
#  find a path from top left to bottom right which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.

class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        if not grid or not grid[0]:
            return 0
        m = len(grid[0])
        n = len(grid)
        for i in range(1, m):
            grid[0][i] += grid[0][i - 1]
        for i in range(1, n):
            grid[i][0] += grid[i - 1][0]
            for j in range(1, m):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[n - 1][m - 1]