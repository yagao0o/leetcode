# Author  :  Yagao0o
# Date    :  2015-01-24
# Source  :  https://oj.leetcode.com/problems/excel-sheet-column-title/

# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
#
# For example:
#
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB
# Credits:
# Special thanks to @ifanchu for adding this problem and creating all test cases.

class Solution:
    # @return a string
    def convertToTitle(self, num):
        num = num
        result = []
        while num > 0:
            current = num % 26
            if current == 0:
                current = 26
            result.insert(0, chr(ord('A') + current - 1))
            num = (num - current) / 26
        return ''.join(result)