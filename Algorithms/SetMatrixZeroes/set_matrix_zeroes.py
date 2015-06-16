# Author  :  Yagao0o
# Date    :  2015-02-15
# Source  :  https://oj.leetcode.com/problems/set-matrix-zeroes/

# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
#
# Follow up:
# Did you use extra space?
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?

class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        length = len(matrix[0])
        height = len(matrix)
        zero_of_i = []
        zero_of_j = []
        for i in range(height):
            for j in range(length):
                if matrix[i][j] == 0:
                    if i not in zero_of_i:
                        zero_of_i.append(i)
                    if j not in zero_of_j:
                        zero_of_j.append(j)
        for i in zero_of_i:
            for j in range(length):
                matrix[i][j] = 0
        for i in range(height):
            for j in zero_of_j:
                matrix[i][j] = 0

a = Solution()
matrix = [[0,1,0],[1,1,1],[0,1,0]]
a.setZeroes(matrix)
print matrix