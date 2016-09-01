# coding: UTF8
# Author  :  Yagao0o
# Date    :  16/9/1
# Description  :  https://leetcode.com/problems/longest-valid-parentheses/


# Given a string containing just the characters '(' and ')',
#   find the length of the longest valid (well-formed) parentheses substring.
#
# For "(()", the longest valid parentheses substring is "()", which has length = 2.
#
# Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        ls = [0]*(len(s) + 1)
        longest = 0
        for i in xrange(1, len(s) + 1):
            if s[i - 1] != '(' and i > 1:
                    if s[i - 2] == '(':
                        ls[i] = 2 + ls[i - 2]
                    else:
                        last_long = ls[i - 1]
                        if i - 2 - last_long >= 0 and s[i - 2 - last_long] == '(':
                            ls[i] = last_long + 2 + ls[i - 2 - last_long]
                    longest = longest if longest > ls[i] else ls[i]
        return longest


