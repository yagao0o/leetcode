# Author  :  Yagao0o
# Date    :  2014-11-3
# Source  :  https://oj.leetcode.com/problems/string-to-integer-atoi/

# Implement atoi to convert a string to an integer.
#
# Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and
# ask yourself what are the possible input cases.
#
# Notes: It is intended for this problem to be specified vaguely (ie, no given input specs).
# You are responsible to gather all the input requirements up front.
#
# spoilers alert... click to show requirements for atoi.
#
# Requirements for atoi:
# The function first discards as many whitespace characters as necessary
# until the first non-whitespace character is found. Then, starting from this character,
# takes an optional initial plus or minus sign followed by as many numerical digits as possible,
# and interprets them as a numerical value.
#
# The string can contain additional characters after those that form the integral number,
# which are ignored and have no effect on the behavior of this function.
#
# If the first sequence of non-whitespace characters in str is not a valid integral number,
# or if no such sequence exists because either str is empty or it contains only whitespace characters,
# no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned.
# If the correct value is out of the range of representable values,
# INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.


class Solution:
    # @return an integer
    def atoi(self, str):
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        result = 0
        str = str.strip()
        is_first = True
        is_positive = 1
        for char in str:
            if char.isdigit():
                result = result * 10 + int(char)
            elif is_first:
                if char == '-':
                    is_positive = -1
                elif char == '+':
                    is_positive = 1
                else:
                    break
            else:
                break
            is_first = False
        result = result * is_positive
        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN
        return result

#COMMENT : not good solution