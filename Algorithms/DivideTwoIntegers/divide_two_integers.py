# Author  :  Yagao0o
# Date    :  2015-02-04
# Source  :  https://oj.leetcode.com/problems/divide-two-integers/

# Divide two integers without using multiplication, division and mod operator.
#
# If it is overflow, return MAX_INT.

class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        result = 0
        positive = 1
        if dividend < 0:
            positive = -1
            dividend = -dividend
        if divisor < 0:
            divisor = -divisor
            if positive == -1:
                positive = 1
            else:
                positive = -1
        current_divisor = divisor
        current_count = 1
        while dividend >= divisor:
            if dividend >= current_divisor:
                result += current_count
                dividend -= current_divisor
                current_divisor <<= 1
                current_count <<= 1
            else:
                current_divisor >>= 1
                current_count >>= 1
        if positive == -1:
            result = -result
        return min(max(- 2147483648, result), 2147483647)