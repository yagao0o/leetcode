# Author  :  Yagao0o
# Date    :  2015-01-22
# Source  :  https://oj.leetcode.com/problems/valid-sudoku/

# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
# http://sudoku.com.au/TheRules.aspx
#
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
# [
# 53..7....
# 6..195...
# .98....6.
# 8...6...3
# 4..8.3..1
# 7...2...6
# .6....28.
# ...419..5
# ....8..79
# ]
#
# A partially filled sudoku which is valid.
#
# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        for i in range(9):
            row = ''
            column = ''
            square = ''
            for j in range(9):
                row = row + board[i][j]
                column = column + board[j][i]
                square = square + board[3 * (i / 3) + j / 3][3 * (i - 3 * (i / 3)) + (j - 3 * (j / 3))]
            if not (self.isValidGroup(row) and self.isValidGroup(column) and self.isValidGroup(square)):
                return False
        return True

    def isValidGroup(self,numbers):
        apperance = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for num in numbers:
            if num.isdigit():
                if apperance[int(num) - 1] == 1:
                    return False
                apperance[int(num) - 1] = 1
        return True