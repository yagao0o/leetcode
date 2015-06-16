# Author  :  Yagao0o
# Date    :  2015-01-22
# Source  :  https://oj.leetcode.com/problems/length-of-last-word/

# Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
#  return the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space characters only.
#
# For example,
# Given s = "Hello World",
# return 5.

class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        length = 0
        if not s:
            return length
        position = len(s) - 1
        while position >= 0:
            if s[position] == ' ':
                if length > 0:
                    return length
            else:
                length += 1
            position -= 1
        return length