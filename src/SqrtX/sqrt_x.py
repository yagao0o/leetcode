# Author  :  Yagao0o
# Date    :  2015-02-15
# Source  :  https://oj.leetcode.com/problems/sqrtx/

# Implement int sqrt(int x).
#
# Compute and return the square root of x.

class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x <= 1:
            return x
        left = 1
        right = x - 1
        middle = (left + right) / 2
        while middle * middle != x and right - left > 1 :
            if middle * middle < x:
                left = middle
            else:
                right = middle
            middle = (left + right) / 2
        return middle
