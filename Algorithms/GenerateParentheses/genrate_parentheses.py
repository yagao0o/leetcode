# Author  :  Yagao0o
# Date    :  2015-02-04
# Source  :  https://oj.leetcode.com/problems/generate-parentheses/

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# "((()))", "(()())", "(())()", "()(())", "()()()"

class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        return self.generate("", n, 0)

    def generate(self, current, left, right):
        if left == 0:
            if right == 0:
                return [current]
            else:
                return [current + ')' * right]
        elif right == 0:
            return self.generate(current + '(', left - 1, 1)
        else:
            return self.generate(current + '(', left - 1, right + 1) + self.generate(current + ')', left, right - 1)