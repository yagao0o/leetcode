# Author  :  Yagao0o
# Date    :  2015-06-14
# Source  :  https://leetcode.com/problems/number-of-islands/

# Given a 2d grid map of '1's (land) and '0's (water),
# count the number of islands. An island is surrounded by water
#  is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#
# 11110
# 11010
# 11000
# 00000
# Answer: 1
#
# Example 2:
#
# 11000
# 11000
# 00100
# 00011
# Answer: 3
#
# Credits:
# Special thanks to @mithmatt for adding this problem and creating all test cases.

class Solution:
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
        land_dic = {}
        counter = 1
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    if i > 0 and grid[i - 1][j] != 0:
                        grid[i][j] = grid[i - 1][j]
                        if j > 0 and grid[i][j - 1] != 0:
                            left = grid[i][j - 1]
                            up =  grid[i - 1][j]
                            if left != up:
                                if up not in land_dic[left]:
                                    land_dic[left].append(up)
                                if left not in land_dic[up]:
                                    land_dic[up].append(left)
                    elif j > 0 and grid[i][j - 1] != 0:
                        grid[i][j] = grid[i][j - 1]
                    else:
                        grid[i][j] = counter
                        land_dic[counter] = []
                        counter += 1
                else:
                    grid[i][j] = 0
        result = 0
        print land_dic
        while land_dic:
            key, connected_list = land_dic.popitem()
            result += 1
            passed = [key]
            while connected_list:
                new = connected_list.pop(0)
                if new not in passed:
                    passed.append(new)
                    connected_list += land_dic.pop(new)
        return result

a = Solution()
s = ["11110111111101011111","11111111111011111111","01111101101111111101","11111111111111111101","11110111111110111101","11111011101111111101","11110111111111101111","01011111100101011111","11111111111111111111","11110001011110101111","11111111111111111111","11111111111011110011","01111111111011111111","11111111110111111111","11111011111111111111","11111111111101111011","11111111111111111111","10111011110111111111","11111111111111111111","11011111111111111111"]
sq = []
for i in s:
    nl = []
    for x in i:
        nl.append(x)
    sq.append(nl)
print a.numIslands(sq)