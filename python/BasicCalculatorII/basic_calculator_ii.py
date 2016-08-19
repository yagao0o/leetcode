# Author  :  Yagao0o
# Date    :  2015/6/24
# Source  :  https://leetcode.com/problems/basic-calculator-ii/

# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces .
# The integer division should truncate toward zero.
#
# You may assume that the given expression is always valid.
#
# Some examples:
# "3+2*2" = 7
# " 3/2 " = 1
# " 3+5 / 2 " = 5
# Note: Do not use the eval built-in library function.
#
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.

class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        ls_num = [0, 0, 0]
        ls_op = ['+','+']
        cons_num = '0123456789'
        for ch in s:
            if ch == ' ':
                continue
            elif ch in '+-*/':
                if ls_op[1] in '+-':
                    ls_num[0] = self.cal(ls_op[0],ls_num[0],ls_num[1])
                    ls_num[1],ls_op[0] = ls_num[2], ls_op[1]
                else:
                    ls_num[1] = self.cal(ls_op[1], ls_num[1], ls_num[2])
                ls_num[2], ls_op[1] = 0, ch
            else:
                ls_num[2] = ls_num[2] * 10 + cons_num.find(ch)
        if ls_op[1] in '+-':
            ls_num[0] = self.cal(ls_op[0],ls_num[0],ls_num[1])
            ls_num[1],ls_op[0] = ls_num[2], ls_op[1]
        else:
            ls_num[1] = self.cal(ls_op[1], ls_num[1], ls_num[2])
        return self.cal(ls_op[0],ls_num[0],ls_num[1])
    def cal(self, op, n1, n2):
        if op =='+':
            return n1 + n2
        if op =='-':
            return n1 - n2
        if op =='*':
            return n1 * n2
        if op =='/':
            return n1 / n2