# Author  :  Yagao0o
# Date    :  2015-02-15
# Source  :  https://oj.leetcode.com/problems/sort-colors/

# Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent,
# with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Note:
# You are not suppose to use the library's sort function for this problem.
#
# Follow up:
# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's,
# then 1's and followed by 2's.
#
# Could you come up with an one-pass algorithm using only constant space?

class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        if not A:
            return
        total_0 = 0
        total_1 = 0
        for i in range(len(A)):
            if A[i] == 1:
                A[i] = A[i - 1]
                A[total_1 + total_0] = 1
                total_1 += 1
            elif A[i] == 0:
                A[i] = A[i - 1]
                A[total_1 + total_0] = 1
                A[total_0] = 0
                total_0 += 1