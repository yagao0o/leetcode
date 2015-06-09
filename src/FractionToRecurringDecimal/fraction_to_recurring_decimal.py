# Author  :  Yagao0o
# Date    :  2015-06-09
# Source  :  https://leetcode.com/problems/fraction-to-recurring-decimal/

# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
#
# If the fractional part is repeating, enclose the repeating part in parentheses.
#
# For example,
#
# Given numerator = 1, denominator = 2, return "0.5".
# Given numerator = 2, denominator = 1, return "2".
# Given numerator = 2, denominator = 3, return "0.(6)".
# Credits:
# Special thanks to @Shangrila for adding this problem and creating all test cases.

class Solution:
    # @param {integer} numerator
    # @param {integer} denominator
    # @return {string}
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return '0'
        result_dict = {}
        not_nagetive = 1
        if numerator < 0:
            not_nagetive, numerator = -1, -numerator
        if denominator < 0:
            not_nagetive, denominator = -not_nagetive, -denominator
        if not_nagetive == -1:
            result = '-'
        else:
            result = ''
        result += str(numerator / denominator)
        remainer = numerator % denominator
        if remainer != 0:
            result += '.'
        while remainer != 0:
            numerator = remainer * 10
            if numerator in result_dict:
                repeat_part = ''
                repeat_part += str(result_dict[numerator][0])
                current = result_dict[numerator][1] * 10
                while current != numerator:
                    repeat_part += str(result_dict[current][0])
                    current = result_dict[current][1] * 10
                result = result.replace(repeat_part,'(' + repeat_part + ')')
                break
            remainer  = numerator % denominator
            new_result = numerator / denominator
            result_dict[numerator] = [new_result,remainer]
            result += str(new_result)
        return result