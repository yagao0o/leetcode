# Author  :  Yagao0o
# Date    :  2015-06-08
# Source  :  https://leetcode.com/problems/evaluate-reverse-polish-notation/

# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.
#
# Some examples:
#   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

class Solution:
    # @param {string[]} tokens
    # @return {integer}
    def evalRPN(self, tokens):
        opers = '+-*/'
        num_stack = []
        for i in tokens:
            if i in opers:
                n2, n1 = num_stack.pop(0), num_stack.pop(0)
                new = self.cal(n1, n2, i)
            else:
                new = int(i)
            num_stack.insert(0, new)
            print num_stack
        return num_stack.pop(0)

    def cal(self, num1, num2, operator):
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return  num1 - num2
        elif operator == '*':
            return num1 * num2
        return int(1.0 * num1 / num2)