# Author  :  Yagao0o
# Date    :  2015-01-06
# Source  :  https://oj.leetcode.com/problems/zigzag-conversion/

# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1:
            return s
        stringList = [];
        for i in range(nRows):
            stringList.append("")
        for num in range(len(s)):
            postion = num % (2 * (nRows - 1))
            if postion >= (nRows - 1):
                postion = 2*(nRows - 1) - postion
            stringList[postion] = stringList[postion] + s[num]
        result = ""
        for str in stringList:
            result += str
        return result