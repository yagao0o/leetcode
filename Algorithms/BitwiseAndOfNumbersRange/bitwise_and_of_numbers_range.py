# Author  :  Yagao0o
# Date    :  2015-06-14
# Source  :  https://leetcode.com/problems/bitwise-and-of-numbers-range/

# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.
#
# For example, given the range [5, 7], you should return 4.
#
# Credits:
# Special thanks to @amrsaqr for adding this problem and creating all test cases.

class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def rangeBitwiseAnd(self, m, n):
        rang = n - m
        counter = 0
        while rang > 0:
            rang >>= 1
            m >>= 1
            counter += 1
        for i in range(counter):
            m <<= 1
        m &= n
        return m
