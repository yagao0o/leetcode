# Author  :  Yagao0o
# Date    :  2015-02-10
# Source  :  https://oj.leetcode.com/problems/multiply-strings/

# Given two numbers represented as strings,
# return multiplication of the numbers as a string.
#
# Note: The numbers can be arbitrarily large and are non-negative.

class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        result = []
        single_multiply_result = {}
        for position in range(len(num2)):
            current_num = ord(num2[len(num2) - 1 - position]) - 48
            if current_num == 0:
                continue
            if current_num not in single_multiply_result:
                remain = 0
                single_multiply = []
                for position_of_num1 in range(len(num1)):
                    current_result = remain + current_num * (ord(num1[len(num1) - 1 - position_of_num1]) - 48)
                    remain = current_result / 10
                    single_multiply.append(current_result - 10 * remain)
                if remain > 0:
                    single_multiply.append(remain)
                single_multiply_result[current_num] = single_multiply
            remain = 0
            for result_position in range(len(single_multiply_result[current_num])):
                current_result = single_multiply_result[current_num][result_position] + remain
                if position + result_position >= len(result):
                    while position + result_position >= len(result):
                        result.append(0)
                else:
                    current_result += result[position + result_position]
                remain = current_result / 10
                result[position + result_position] = current_result - 10 * remain
            if remain > 0:
                result.append(remain)
        result_string = ""
        is_first = True
        for position in range(len(result)):
            current_num = result[len(result) - 1 - position]
            if is_first and current_num == 0:
                continue
            result_string += chr(48 + current_num)
            is_first = False
        return result_string if result_string != "" else "0"
