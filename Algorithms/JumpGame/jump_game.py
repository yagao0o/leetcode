# Author  :  Yagao0o
# Date    :  2015-02-12
# Source  :  https://oj.leetcode.com/problems/jump-game/

# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Determine if you are able to reach the last index.
#
# For example:
# A = [2,3,1,1,4], return true.
#
# A = [3,2,1,0,4], return false.

class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        if not A:
            return False
        most_far = 0
        for position in range(len(A)):
            if position > most_far:
                break
            most_far = most_far if A[position] + position < most_far else A[position] + position
        if most_far >= len(A) - 1:
            return True
        return False