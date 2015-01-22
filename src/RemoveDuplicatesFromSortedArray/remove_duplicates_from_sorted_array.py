# Author  :  Yagao0o
# Date    :  2015-01-22
# Source  :  https://oj.leetcode.com/problems/remove-duplicates-from-sorted-array/

# Given a sorted array, remove the duplicates in place such that
# each element appear only once and return the new length.
#
# Do not allocate extra space for another array, you must do this in place with constant memory.
#
# For example,
# Given input array A = [1,1,2],
#
# Your function should return length = 2, and A is now [1,2].


class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        current = 0
        for i in range(1, len(A)):
            if A[current]!= A[i]:
                current += 1
                A[current] = A[i]
        A = A[:current]
        return current + 1