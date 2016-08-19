# Author  :  yagao0o
# Date    :  2015/10/5
# Source  :  https://leetcode.com/problems/regular-expression-matching/


# Implement regular expression matching with support for '.' and '*'.
# 
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# 
# The matching should cover the entire input string (not partial).
# 
# The function prototype should be:
# bool isMatch(const char *s, const char *p)
# 
# Some examples:
# isMatch("aa","a") -> false
# isMatch("aa","aa") -> true
# isMatch("aaa","aa") -> false
# isMatch("aa", "a*") -> true
# isMatch("aa", ".*") -> true
# isMatch("ab", ".*") -> true
# isMatch("aab", "c*a*b") -> true


class Solution(object):
    cache = {}

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if (s, p) in self.cache:
            return self.cache[(s, p)]
        if not s and not p:
            return True
        else:
            if not p:
                self.cache[(s, p)] = False
                return False
            if not s and p[-1] != '*':
                self.cache[(s, p)] = False
                return False

        if p[-1] != '*':
            if p[-1] == '.' or p[-1] == s[-1]:
                result = self.isMatch(s[:-1], p[:-1])
                self.cache[(s, p)] = result
                return result
            else:
                self.cache[(s, p)] = False
                return False
        else:
            start = 0
            result = self.isMatch(s, p[:-2])
            while not result and start < len(s):
                start += 1
                if p[-2] != '.' and p[-2] != s[-start]:
                    break
                result = self.isMatch(s[:-start] , p[:-2])
            self.cache[(s, p)] = result
            return result