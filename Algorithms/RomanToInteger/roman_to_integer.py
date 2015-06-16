# Author  :  Yagao0o
# Date    :  2014-11-6
# Source  :  https://oj.leetcode.com/problems/roman-to-integer/


# Given an integer, convert it to a roman numeral.
#
# Input is guaranteed to be within the range from 1 to 3999.
# Roman to int

# Some materials of wikipedia
# http://en.wikipedia.org/wiki/Roman_numerals

# Symbol	Value
# I	1
# V	5
# X	10
# L	50
# C	100
# D	500
# M	1,000

# Numbers are formed by combining symbols and adding the values. So II is two ones, i.e. 2,
# and XIII is a ten and three ones, i.e. 13. There is no zero in this system,
# so 207, for example, is CCVII, using the symbols for two hundreds, a five and two ones.
# 1066 is MLXVI, one thousand, fifty and ten, a five and a one.
#
# Symbols are placed from left to right in order of value, starting with the largest.
# However, in a few specific cases,[2] to avoid four characters being repeated in succession (such as IIII or XXXX)
# these can be reduced using subtractive notation as follows:[3][4]
#
# the numeral I can be placed before V and X to make 4 units (IV) and 9 units (IX) respectively
# X can be placed before L and C to make 40 (XL) and 90 (XC) respectively
# C can be placed before D and M to make 400 (CD) and 900 (CM) according to the same pattern[5]


class Solution:
    # @return an integer
    def romanToInt(self, s):
        total = 0
        current = 0
        numberDic = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        current = numberDic[s[0]]
        for number in range(1, len(s)):
            if numberDic[s[number]] <= numberDic[s[number - 1]]:
                total += current
                current = numberDic[s[number]]
            else:
                total += numberDic[s[number]] - current
                current = 0
        total += current
        return total
