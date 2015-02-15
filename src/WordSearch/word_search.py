# Author  :  Yagao0o
# Date    :  2015-02-15
# Source  :  https://oj.leetcode.com/problems/word-search/

# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring.
# The same letter cell may not be used more than once.
#
# For example,
# Given board =
#
# [
#   ["ABCE"],
#   ["SFCS"],
#   ["ADEE"]
# ]
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.

# yagao0o Note: The example and the note given is not exactly same with test case in OJ,
#               actually it should be a list of string

class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.find_chars(board, word[1:], [[i,j]], i, j):
                    return True
        return False

    def find_chars(self, board, word, char_list , last_row, last_column):
        if not word:
            return True
        if last_column > 0 and board[last_row][last_column - 1] == word[0] and \
                not [last_row, last_column - 1] in char_list and \
                self.find_chars(board, word[1:], char_list + [[last_row, last_column - 1]], last_row, last_column - 1):
            return True
        if last_column < len(board[0]) - 1 and board[last_row][last_column + 1] == word[0] and \
                not [last_row, last_column + 1] in char_list and \
                self.find_chars(board, word[1:], char_list + [[last_row, last_column + 1]], last_row, last_column + 1):
            return True
        if last_row > 0 and board[last_row - 1][last_column] == word[0] and \
                not [last_row - 1, last_column] in char_list and \
            self.find_chars(board, word[1:], char_list + [[last_row - 1, last_column]], last_row - 1, last_column):
            return True
        if last_row < len(board) - 1 and board[last_row + 1][last_column] == word[0] and \
                not [last_row + 1, last_column] in char_list and \
            self.find_chars(board, word[1:], char_list + [[last_row + 1, last_column]], last_row + 1, last_column):
            return True
        return False