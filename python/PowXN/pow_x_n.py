# Author  :  Yagao0o
# Date    :  2015-02-11
# Source  :  https://oj.leetcode.com/problems/powx-n/

# Implement pow(x, n).

class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        result = 1
        current = x
        while n > 0:
            if n % 2 == 1:
                result = result * current
            current = current * current
            n /= 2
        return result