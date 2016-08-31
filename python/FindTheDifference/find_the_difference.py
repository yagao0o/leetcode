# coding: UTF8
# Author  :  Yagao0o
# Date    :  16/8/31
# Description  :  https://leetcode.com/contest/2/problems/find-the-difference/

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic = {}
        for char in s:
            dic[char] = dic.get(char, 0) + 1
        for char in t:
            if dic.get(char, 0) == 0:
                return char
            else:
                dic[char] -= 1