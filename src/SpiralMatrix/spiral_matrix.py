# Author  :  Yagao0o
# Date    :  2015-02-12
# Source  :  https://oj.leetcode.com/problems/spiral-matrix/

# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
# For example,
# Given the following matrix:
#
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# You should return [1,2,3,6,9,8,7,4,5].


class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        x = 0
        y = len(matrix[0]) - 1
        direction = 1
        result = []
        total_numbers = len(matrix) * len(matrix[0])
        for i in range(len(matrix[0])):
            result.append(matrix[0][i])
        edge_m = len(matrix[0]) - 1
        edge_n = len(matrix) - 1
        edge_remain = edge_n
        while len(result) < total_numbers:
            x, y = self.move_to_next(x, y, direction)
            print x,y,'|',matrix[x][y],'|',direction,'|',edge_m, edge_n,edge_remain
            result.append(matrix[x][y])
            edge_remain -= 1
            if edge_remain == 0:
                direction = (direction + 1) % 4
                if direction % 2 == 1:
                    edge_m -= 1
                    edge_n -= 1
                    edge_remain = edge_n
                else:
                    edge_remain = edge_m
        return result

    def move_to_next(self, x, y, direction):
        # 0 -> 1 |  2 <-  3 ^
        if direction <= 1:
            if direction == 0:
                return x, y + 1
            return x + 1, y
        elif direction == 2:
            return x, y - 1
        return x - 1, y

#TODO it could optimize about 30% running time.