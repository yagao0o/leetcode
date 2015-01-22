# Author  :  Yagao0o
# Date    :  2015-01-22
# Source  :  https://oj.leetcode.com/problems/add-binary/

# Given two binary strings, return their sum (also a binary string).
#
# For example,
# a = "11"
# b = "1"
# Return "100".

class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        result = ''
        a = a[len(a)::-1]
        b = b[len(b)::-1]
        add = 0
        if len(a) > len(b):
            longer = a
        else:
            longer = b
        for position in range(min(len(a),len(b))):
            current =  int(a[position] ) + int(b[position]) + add
            if current >= 2:
                add = 1
                result += str(current - 2)
            else:
                add = 0
                result += str(current)
        position += 1
        while position < len(longer):
            if add == 0:
                result += longer[position]
            else:
                if longer[position] == '1':
                    add = 1
                    result += '0'
                else:
                    add = 0
                    result += '1'
            position += 1
        if add == 1:
            result += '1'
        return result[len(result)::-1]