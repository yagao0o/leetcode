# Author  :  Yagao0o
# Date    :  2015-02-19
# Source  :  https://oj.leetcode.com/problems/decode-ways/

# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message containing digits, determine the total number of ways to decode it.
#
# For example,
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
#
# The number of ways decoding "12" is 2.

class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        before_last = 1
        last = 1
        const_one_to_six = '123456'
        for position in range(1, len(s)):
            if s[position] == '0':
                current = before_last
                before_last = 0
                last = current
            else:
                current = last
                if s[position - 1] == '1'or (s[position - 1] == '2' and s[current] in const_one_to_six):
                    current += before_last
                before_last = last
                last = current
        return current



a = Solution()
print a.numDecodings('11111')
print a.numDecodings('10101')
print a.numDecodings('1216')