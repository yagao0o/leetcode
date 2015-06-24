# Author  :  Yagao0o
# Date    :  2015/6/24
# Source  :  https://leetcode.com/problems/basic-calculator/

# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string may contain open ( and closing parentheses ),
# the plus + or minus sign -, non-negative integers and empty spaces .
#
# You may assume that the given expression is always valid.
#
# Some examples:
# "1 + 1" = 2
# " 2-1 + 2 " = 3
# "(1+(4+5+2)-3)+(6+8)" = 23
# Note: Do not use the eval built-in library function.

class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        CONS_NUMS = "0123456789"
        CONS_OPER = "+-"
        cal_stack = []
        c_value = 0
        for char in s:
            if char == ' ':
                continue
            if CONS_NUMS.find(char) >= 0:
                c_value = c_value * 10 + CONS_NUMS.find(char)
            else:
                if char == '(':
                    self.in_stack(cal_stack, char)
                elif char == ')':
                    op = cal_stack.pop(0)
                    while op != '(':
                        first_num = cal_stack.pop(0)
                        c_value = self.simple_cal(op, first_num, c_value)
                        op = cal_stack.pop(0)
                elif char in CONS_OPER:
                    if cal_stack and cal_stack[0] in CONS_OPER:
                        op = cal_stack.pop(0)
                        first_num = cal_stack.pop(0)
                        c_value = self.simple_cal(op, first_num, c_value)
                    self.in_stack(cal_stack, c_value)
                    self.in_stack(cal_stack, char)
                    c_value = 0
        if cal_stack and cal_stack[0] in CONS_OPER:
            op = cal_stack.pop(0)
            first_num = cal_stack.pop(0)
            c_value = self.simple_cal(op, first_num, c_value)
        return c_value

    def in_stack(self, cal_stack, val):
        if cal_stack:
            cal_stack.insert(0, val)
        else:
            cal_stack.append(val)

    def simple_cal(self, op, first_n, second_n):
        if op == '+':
            return first_n + second_n
        return first_n - second_n
