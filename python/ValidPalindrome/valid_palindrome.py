# Author  :  Yagao0o
# Date    :  2014-11-5
# Source  :  https://oj.leetcode.com/problems/valid-palindrome/

# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.
#
# Note:
# Have you consider that the string might be empty? This is a good question to ask during an interview.
#
# For the purpose of this problem, we define empty string as valid palindrome.


class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        punc = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ "
        new_string = ""
        for char in s:
            if char not in punc:
                new_string += char
        left = 0
        right = len(new_string) - 1
        s = new_string.lower()
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right += -1
        return True

#Came up Compile Error when I use 'import string'
#don't know why, To be figure out