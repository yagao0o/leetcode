# Author  :  Yagao0o
# Date    :  2015/8/6
# Source  :  https://leetcode.com/problems/power-of-two/

# Given an integer, write a function to determine if it is a power of two.
#
# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        start = 1
        while start < n:
            start = start << 1
        if start == n:
            return True
        return False