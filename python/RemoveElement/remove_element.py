# Author  :  Yagao0o
# Date    :  2015-01-22
# Source  :  https://oj.leetcode.com/problems/remove-element/

# Given an array and a value, remove all instances of that value in place and return the new length.
#
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        number = 0
        for position in range(len(A)):
            if A[position] != elem:
                A[number] = A[position]
                number += 1
        A = A[:number]
        return number