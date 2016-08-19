# Author  :  Yagao0o
# Date    :  2015-02-28
# Source  :  https://oj.leetcode.com/problems/validate-binary-search-tree/

# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        if not root:
            return True
        in_order_list = []
        self.get_in_order_list(in_order_list, root)
        i = 0
        while i < len(in_order_list) - 1:
            if in_order_list[i] >= in_order_list[i + 1]:
                return False
            i += 1
        return True

    def get_in_order_list(self, list, root):
        if root.left:
            self.get_in_order_list(list, root.left)
        list.append(root.val)
        if root.right:
            self.get_in_order_list(list, root.right)