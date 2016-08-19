# Author  :  Yagao0o
# Date    :  2014-11-7
# Source  :  https://oj.leetcode.com/problems/integer-to-roman/


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
    # @return a string
    def intToRoman(self, num):
        char_of_place = ['IVX', 'XLC', 'CDM', 'M']
        number_dic = [[], [0], [0, 0], [0, 0, 0], [0, 1], [1], [1, 0], [1, 0, 0], [1, 0, 0, 0], [0, 2]]
        num_str = str(num)
        length = len(num_str)
        result = ''
        for place in range(length):
            for number in number_dic[int(num_str[place])]:
                result += char_of_place[length - place - 1][number]
        return result

