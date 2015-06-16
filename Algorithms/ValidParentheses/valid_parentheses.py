# Author  :  Yagao0o
# Date    :  2015-01-06
# Source  :  https://oj.leetcode.com/problems/valid-parentheses/

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

class Solution:
    # @return a boolean
    def isValid(self, s):
        left = '([{'
        right = ')]}'
        stack = []
        for pare in s:
            if pare in left:
                stack.insert(0,pare)
            else:
                if not stack or stack[0] != left[right.find(pare)]:
                    return False
                stack.pop(0)
        if stack:
            return False
        return True