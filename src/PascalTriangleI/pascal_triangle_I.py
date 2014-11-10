# Author  :  Yagao0o
# Date    :  2014-11-10
# Source  :  https://oj.leetcode.com/problems/pascals-triangle/

# Given numRows, generate the first numRows of Pascal's triangle.
#
# For example, given numRows = 5,
# Return
#
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        result = []
        for i in range(numRows):
            if i == 0:
                result.append([1])
            elif i == 1:
                result.append([1, 1])
            else:
                new_array = [1]
                for new_number in range(i - 1):
                    new_array.append(result[i - 1][new_number] + result[i - 1][new_number + 1])
                new_array.append(1)
                result.append(new_array)
        return result