# Author  :  Yagao0o
# Date    :  2015-03-01
# Source  :  https://oj.leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Given preorder and inorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        return self.build_binary_tree(preorder, 0, inorder, 0, len(preorder))

    def build_binary_tree(self, preorder, preorder_left_flag, inorder, inorder_left_flag, length):
        if length == 0:
            return None
        if length == 1:
            return TreeNode(preorder[preorder_left_flag])
        else:
            root_place = inorder.index(preorder[preorder_left_flag])
            left_length = root_place - inorder_left_flag
            new_root = TreeNode(preorder[preorder_left_flag])
            new_root.left = self.build_binary_tree(preorder, preorder_left_flag + 1, inorder, inorder_left_flag,
                                                   left_length)
            new_root.right = self.build_binary_tree(preorder, preorder_left_flag + 1 + left_length, inorder,
                                                    inorder_left_flag + 1 + left_length, length - left_length - 1)
            return new_root