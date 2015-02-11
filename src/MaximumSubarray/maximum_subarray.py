# Author  :  Yagao0o
# Date    :  2015-02-11
# Source  :  https://oj.leetcode.com/problems/maximum-subarray/

# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
#
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.
#
# click to show more practice.
#
# More practice:
# If you have figured out the O(n) solution,
# try coding another solution using the divide and conquer approach, which is more subtle.

# YagaoNote:
#  O(n) - DP ,
#  O(nlogn) - Divide and conquer

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        max = A[0]
        max_of_last = A[0]
        for i in range(1, len(A)):
            max_of_last = A[i] if max_of_last <= 0 else A[i] + max_of_last
            if max < max_of_last:
                max = max_of_last
        return max