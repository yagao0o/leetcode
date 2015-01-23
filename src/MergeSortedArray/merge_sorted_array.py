# Author  :  Yagao0o
# Date    :  2015-01-23
# Source  :  https://oj.leetcode.com/problems/merge-sorted-array/

# Given two sorted integer arrays A and B, merge B into A as one sorted array.
#
# Note:
# You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B.
# The number of elements initialized in A and B are m and n respectively.

class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        position_a = m - 1
        position_b = n - 1
        while position_a>= 0 and position_b >= 0:
            if A[position_a] > B[position_b]:
                A[position_a + position_b + 1] = A[position_a]
                position_a -= 1
            else:
                A[position_a + position_b + 1] = B[position_b]
                position_b -= 1
        while position_b >= 0:
            A[position_b] = B[position_b]
            position_b -= 1
        return A