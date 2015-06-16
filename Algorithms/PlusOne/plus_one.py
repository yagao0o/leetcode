# Author  :  Yagao0o
# Date    :  2014-12-15
# Source  :  https://oj.leetcode.com/problems/plus-one/

# Given a non-negative number represented as an array of digits, plus one to the number.
#
# The digits are stored such that the most significant digit is at the head of the list.

class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        add = 1
        for position in range(1,len(digits) + 1):
            if add == 1:
                digits[-position] += 1
                if digits[-position] == 10:
                    digits[-position] = 0
                    add = 1
                else:
                    add = 0
        if add == 1:
            digits.insert(0,1)
        return digits

