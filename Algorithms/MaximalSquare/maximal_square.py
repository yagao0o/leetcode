# Author  :  Yagao0o
# Date    :  2015/6/17
# Source  :  https://leetcode.com/problems/maximal-square/

# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.
#
# For example, given the following matrix:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# Return 4 [(1,2),(2,3)].
# Credits:
# Special thanks to @Freezen for adding this problem and creating all test cases.

class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        if len(matrix) == 1 or len(matrix[0]) == 1:
            for i in matrix:
                for j in i:
                    if j == '1':
                        return 1
            return 0
        result_square = []
        max_square = 0
        for i in range(len(matrix)):
            result_square.append([0] * len(matrix[i]))
            if matrix[i][0] == '0':
                result_square[i][0] = 0
            else:
                max_square = 1
                result_square[i][0] = 1
        for i in range(1, len(matrix[0])):
            if matrix[0][i] == '0':
                result_square[0][i] = 0
            else:
                max_square = 1
                result_square[0][i] = 1
        for i in range(1,len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == '0':
                    result_square[i][j] = 0
                    continue
                result_square[i][j] = 1
                up_left = result_square[i - 1][j - 1]
                if up_left > 0:
                    for step in range(up_left):
                        if result_square[i][j - step - 1] > 0 and result_square[i - step - 1][j] > 0:
                            result_square[i][j] += 1
                        else:
                            break
                max_square = max(max_square, result_square[i][j])
        return max_square * max_square