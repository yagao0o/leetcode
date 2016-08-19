# Author  :  Yagao0o
# Date    :  2015-02-17
# Source  :  https://oj.leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?
#
# For example,
# Given sorted array A = [1,1,1,2,2,3],
#
# Your function should return length = 5, and A is now [1,1,2,2,3].

class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        length = len(A)
        if length <= 2:
            return length
        position = 2
        while position < length:
            if A[position] == A[position - 2]:
                A.pop(position)
                length -= 1
            else:
                position += 1
        return length