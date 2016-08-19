# Author  :  Yagao0o
# Date    :  2015-02-14
# Source  :  https://oj.leetcode.com/problems/unique-paths-ii/

# Follow up for "Unique Paths":
#
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
#
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
#
# For example,
# There is one obstacle in the middle of a 3x3 grid as illustrated below.
#
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# The total number of unique paths is 2.
#
# Note: m and n will be at most 100.

class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        if obstacleGrid[0][0] == 0:
            obstacleGrid[0][0] = 1
        else:
            return 0
        length = len(obstacleGrid[0])
        height = len(obstacleGrid)
        for i in range(1, length):
            obstacleGrid[0][i] = 0 if obstacleGrid[0][i] == 1 else obstacleGrid[0][i - 1]
        for i in range(1, height):
            obstacleGrid[i][0] = 0 if obstacleGrid[i][0] == 1 else obstacleGrid[i - 1][0]
            for j in range(1, length):
                obstacleGrid[i][j] = 0 if obstacleGrid[i][j] == 1 else obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
        return obstacleGrid[height - 1][length - 1]