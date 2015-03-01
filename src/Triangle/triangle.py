# Author  :  Yagao0o
# Date    :  2015-03-01
# Source  :  https://oj.leetcode.com/problems/triangle/

# Given a triangle, find the minimum path sum from top to bottom.
# Each step you may move to adjacent numbers on the row below.
#
# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#
# Note:
# Bonus point if you are able to do this using only O(n) extra space,
# where n is the total number of rows in the triangle.

class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if not triangle:
            return 0
        if len(triangle) == 1:
            return triangle[0][0]
        current = [triangle[0][0]]
        for line in range(1, len(triangle)):
            current.append(triangle[line][line] + current[line - 1])
            j = line - 1
            while j > 0:
                current[j] = min(current[j], current[j - 1]) + triangle[line][j]
                j -= 1
            current[0] += triangle[line][0]
        return min(current)

a = Solution()
tri = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print a.minimumTotal(tri)