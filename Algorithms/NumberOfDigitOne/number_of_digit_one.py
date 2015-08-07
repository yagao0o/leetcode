# Author  :  Yagao0o
# Date    :  2015/8/7
# Source  :  https://leetcode.com/problems/number-of-digit-one/

# Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.
#
# For example:
# Given n = 13,
# Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
#
# Hint:
#
# Beware of overflow.

class Solution:
    # @param {integer} n
    # @return {integer}
    def countDigitOne(self, n):
        current_base = 1
        total_count = 0
        while current_base <= n:
            total_count += n / (current_base * 10) * current_base
            if (n / current_base) % 10 > 1:
                total_count += current_base
            elif (n / current_base) % 10 == 1:
                total_count += (n % current_base) + 1
            current_base *= 10
        return total_count