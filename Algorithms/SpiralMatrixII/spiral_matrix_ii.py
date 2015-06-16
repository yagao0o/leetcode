# Author  :  Yagao0o
# Date    :  2015-02-12
# Source  :  https://oj.leetcode.com/problems/spiral-matrix-ii/

# Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
#
# For example,
# Given n = 3,
#
# You should return the following matrix:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
#  ]

class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        result = []
        if n == 0:
            return result
        for i in range(n):
            new_row = []
            for j in range(n):
                new_row.append(0)
            result.append(new_row)
        x = 0
        y = n - 1
        direction = 1
        current = 1
        for i in range(n):
            result[0][i] = current
            current += 1
        edge_m = n - 1
        edge_remain = edge_m
        while current <= n * n:
            x, y = self.move_to_next(x, y, direction)
            result[x][y] = current
            current += 1
            edge_remain -= 1
            if edge_remain == 0:
                direction = (direction + 1) % 4
                if direction % 2 == 1:
                    edge_m -= 1
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