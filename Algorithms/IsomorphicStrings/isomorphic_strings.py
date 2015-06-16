# Author  :  Yagao0o
# Date    :  2015-06-16
# Source  :  https://leetcode.com/problems/isomorphic-strings/

# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character but a character may map to itself.
#
# For example,
# Given "egg", "add", return true.
#
# Given "foo", "bar", return false.
#
# Given "paper", "title", return true.
#
# Note:
# You may assume both s and t have the same length.

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        dic_s_t = {}
        dic_t_s = {}
        for i in range(len(s)):
            sc = s[i]
            tc = t[i]
            if sc not in dic_s_t:
                dic_s_t[sc] = tc
            else:
                if dic_s_t[sc] != tc:
                    return False
            if tc not in dic_t_s:
                dic_t_s[tc] = sc
            else:
                if dic_t_s[tc] != sc:
                    return False
        return True