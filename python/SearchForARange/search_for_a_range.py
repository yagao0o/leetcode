# Author  :  Yagao0o
# Date    :  2015-02-05
# Source  :  https://oj.leetcode.com/problems/search-for-a-range/

# Given a sorted array of integers, find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].


class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        return [self.search_left_side(A, target, 0, len(A) - 1), self.search_right_side(A, target, 0, len(A) - 1)]

    def search_left_side(self, A, target, left, right):
        if left == right and A[left] != target:
            return -1
        middle = (left + right) / 2
        if A[middle] == target:
            if middle == 0 or A[middle - 1] != target:
                return middle
            return self.search_left_side(A, target, left, middle)
        elif A[middle] < target:
            return self.search_left_side(A, target, middle + 1, right)
        return self.search_left_side(A, target, left, middle)

    def search_right_side(self, A, target, left, right):
        if left == right and A[right] != target:
            return -1
        middle = (left + right) / 2
        if A[middle] == target:
            if middle == len(A) - 1 or A[middle + 1] != target:
                return middle
            return self.search_right_side(A, target, middle + 1, right)
        elif A[middle] > target:
            return self.search_right_side(A, target, left, middle)
        return self.search_right_side(A, target, middle + 1, right)