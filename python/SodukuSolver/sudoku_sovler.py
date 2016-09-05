# coding: UTF8
# Author  :  Yagao0o
# Date    :  16/9/5
# Description  :

# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# Empty cells are indicated by the character '.'.
#
# You may assume that there will be only one unique solution.
#
# 53..7....
# 6..195...
# .98....6.
# 8...6...3
# 4..8.3..1
# 7...2...6
# .6....28.
# ...419..5
# ....8..79
#
# A sudoku puzzle...
#
# 534678912
# 672195348
# 198342567
# 859761423
# 426853791
# 713924856
# 961537284
# 287419635
# 345286179
#
# ...and its solution numbers marked in red.


class Solution(object):
    def __init__(self):
        self.row_set = []
        self.column_set = []
        self.square_set = []
        self.solver_board = []

    def print_board(self):
        for line_nums in self.solver_board:
            for num in line_nums:
                print str(num) + ' ',
            print

    def to_previous(self, board, row, column):
        while True:
            column -= 1
            if column == -1:
                column = 8
                row -= 1
            if board[row][column] == '.':
                break
        return row, column

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        for i in xrange(9):
            self.row_set.append({1, 2, 3, 4, 5, 6, 7, 8, 9})
            self.column_set.append({1, 2, 3, 4, 5, 6, 7, 8, 9})
            self.square_set.append({1, 2, 3, 4, 5, 6, 7, 8, 9})
            self.solver_board.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

        for i in xrange(9):
            for j in xrange(9):
                if board[i][j] == '.':
                    continue
                num = int(board[i][j])
                self.row_set[i].remove(num)
                self.column_set[j].remove(num)
                self.square_set[i/3*3+j/3].remove(num)
                self.solver_board[i][j] = num

        # solve
        i = 0
        j = 0
        while True:
            # isEditable
            if board[i][j] == '.':
                current = self.solver_board[i][j]
                target_nums = self.column_set[j]
                target_nums = target_nums.intersection(self.row_set[i])
                target_nums = target_nums.intersection(self.square_set[i/3*3+j/3])
                next_num = 0
                for n in xrange(current + 1, 10):
                    if n in target_nums:
                        next_num = n
                        break
                if current > 0:
                    self.row_set[i].add(current)
                    self.column_set[j].add(current)
                    self.square_set[i/3*3+j/3].add(current)
                if next_num > 0:
                    self.solver_board[i][j] = next_num
                    self.row_set[i].remove(next_num)
                    self.column_set[j].remove(next_num)
                    self.square_set[i/3*3+j/3].remove(next_num)
                else:
                    self.solver_board[i][j] = 0
                    i, j = self.to_previous(board, i, j)
                    continue
            j += 1
            if j == 9:
                if i == 8:
                    break
                else:
                    j = 0
                    i += 1
        for i in xrange(9):
            for j in xrange(9):
                board[i][j] = str(self.solver_board[i][j])
