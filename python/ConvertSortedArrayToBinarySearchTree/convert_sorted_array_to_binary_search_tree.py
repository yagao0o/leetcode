# Author  :  Yagao0o
# Date    :  2015-03-01
# Source  :  https://oj.leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        return self.build_bst_from_sorted_array(num, 0, len(num))

    def build_bst_from_sorted_array(self, list, start, length):
        if length == 0:
            return None
        elif length == 1:
            return TreeNode(list[start])
        else:
            middle = start + length / 2
            new_root = TreeNode(list[middle])
            new_root.left = self.build_bst_from_sorted_array(list, start, middle - start)
            new_root.right = self.build_bst_from_sorted_array(list, middle + 1, length - length/2 - 1)
            return new_root