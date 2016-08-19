# Author  :  Yagao0o
# Date    :  2015-02-06
# Source  :  https://oj.leetcode.com/problems/search-insert-position/

# Given a sorted array and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
#
# You may assume no duplicates in the array.
#
# Here are few examples.
# [1,3,5,6], 5 -> 2
# [1,3,5,6], 2 -> 1
# [1,3,5,6], 7 -> 4
# [1,3,5,6], 0 -> 0

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        if target <= A[0]:
            return 0
        elif target > A[len(A) - 1]:
            return len(A)
        return self.find_target(A, target, 0, len(A) - 1)
    def find_target(self, A, target, left, right):
        if left == right:
            if A[left] == target:
                return left
            elif A[left] > target:
                return left
            return left + 1
        middle = (left + right) / 2
        if A[middle] == target:
            return middle
        elif A[middle] > target:
            return self.find_target(A, target, left, middle)
        return self.find_target(A, target, middle + 1, right)