# Author  :  Yagao0o
# Date    :  2015-01-24
# Source  :  https://oj.leetcode.com/problems/factorial-trailing-zeroes/

# Given an integer n, return the number of trailing zeroes in n!.
#
# Note: Your solution should be in logarithmic time complexity.
#
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.
class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        result = 0
        while n > 0:
            n /= 5
            result += n
        return result