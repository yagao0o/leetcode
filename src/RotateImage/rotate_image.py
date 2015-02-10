# Author  :  Yagao0o
# Date    :  2015-02-10
# Source  :  https://oj.leetcode.com/problems/rotate-image/

# You are given an n x n 2D matrix representing an image.
#
# Rotate the image by 90 degrees (clockwise).
#
# Follow up:
# Could you do this in-place?

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        length = len(matrix)
        if length % 2 != 0:
            half_length = (length + 1) / 2
        else:
            half_length = length / 2
        for i in range(length / 2):
            for j in range(half_length):
                temp = matrix[i][j]
                matrix[i][j] = matrix[length - 1 - j][i]
                matrix[length - 1 - j][i] = matrix[length - 1 - i][length - 1 - j]
                matrix[length - 1 - i][length - 1 - j] = matrix[j][length - 1 - i]
                matrix[j][length - 1 - i] = temp
        return matrix