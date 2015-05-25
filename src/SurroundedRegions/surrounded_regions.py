# Author  :  Yagao0o
# Date    :  2015-05-25
# Source  :  https://leetcode.com/problems/surrounded-regions/

# Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
# For example,
# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:
#
# X X X X
# X X X X
# X X X X
# X O X X

class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solve(self, board):
        if not board:
            return
        # travel the whole board to separate the zone in board
        # mark connected zone by number
        zone_dict = {}
        zone_index = 0
        for row in range(len(board)):
            for column in range(len(board[row])):
                if board[row][column] == 'O':
                    up = board[row - 1][column] if row > 0 else None
                    left = board[row][column - 1] if column > 0 else None
                    if (not up or up == 'X') and (not left or left == 'X'):
                        board[row][column] = zone_index
                        zone_dict[zone_index] = [[row, column]]
                        zone_index += 1
                    else:
                        if up != None and up != 'X':
                            board[row][column] = up
                            zone_dict[up].append([row,column])
                            if left and left != 'X' and left != up:
                                zone_list = zone_dict.pop(left)
                                zone_dict[up] += zone_list
                                for point in zone_list:
                                    board[point[0]][point[1]] = up
                        elif left != None and left != 'X':
                            board[row][column] = left
                            zone_dict[left].append([row,column])
        # travel the board find zhe zone which haven't been surrounded
        boarder_set = set([])
        for row in range(len(board)):
            if board[row][0] != 'X':
                boarder_set.add(board[row][0])
            if board[row][-1] != 'X':
                boarder_set.add(board[row][-1])
        for column in range(len(board[0])):
            if board[0][column] != 'X':
                boarder_set.add(board[0][column])
            if board[-1][column] != 'X':
                boarder_set.add(board[-1][column])
        print boarder_set
        # replace the square haven't been surrounded by O
        for zone_index in boarder_set:
            for square in zone_dict.pop(zone_index):
                board[square[0]][square[1]] = 'O'
        # replace the other by X
        for zone_index in zone_dict:
            for square in zone_dict[zone_index]:
                board[square[0]][square[1]] = 'X'
        return board