# Author  :  Yagao0o
# Date    :  2015-02-15
# Source  :  https://oj.leetcode.com/problems/search-a-2d-matrix/

# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# For example,
#
# Consider the following matrix:
#
# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# Given target = 3, return true.

class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        top = 0
        bottom = len(matrix) - 1
        level = (top + bottom) / 2
        while top < bottom:
            if target < matrix[level][0]:
                bottom = level - 1
            elif target > matrix[level][len(matrix[0]) - 1]:
                top = level + 1
            else:
                top = level
                bottom = level
            level = (top + bottom) / 2
        left = 0
        right = len(matrix[0]) - 1
        middle = (left + right) / 2
        while left < right:
            if target == matrix[level][middle]:
                left = middle
                right = middle
            elif target < matrix[level][middle]:
                right = middle - 1
            else:
                left = middle + 1
            middle = (left + right) / 2
        if matrix[level][middle] == target:
            return True
        return False