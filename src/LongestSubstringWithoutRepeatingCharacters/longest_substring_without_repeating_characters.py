# Author  :  Yagao0o
# Date    :  2015-01-26
# Source  :  https://oj.leetcode.com/problems/longest-substring-without-repeating-characters/

# Given a string, find the length of the longest substring without repeating characters.
# For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.
# For "bbbbb" the longest substring is "b", with the length of 1.

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        current_chars = []
        max_long = 0
        for char in s:
            if char in current_chars:
                current_chars = current_chars[current_chars.index(char) + 1:] + [char]
            else:
                current_chars.append(char)
                if len(current_chars) > max_long:
                    max_long = len(current_chars)
        return max_long