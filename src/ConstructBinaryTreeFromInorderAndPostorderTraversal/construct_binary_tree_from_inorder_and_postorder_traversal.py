# Author  :  Yagao0o
# Date    :  2015-03-01
# Source  :  https://oj.leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# Given inorder and postorder traversal of a tree, construct the binary tree.
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
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        return self.build_binary_tree(inorder, 0, postorder, 0, len(inorder))

    def build_binary_tree(self, inorder, inorder_left_flag, postorder, postorder_left_flag, length):
        if length == 0:
            return None
        if length == 1:
            return TreeNode(postorder[postorder_left_flag])
        else:
            root_place = inorder.index(postorder[postorder_left_flag + length - 1])
            left_length = root_place - inorder_left_flag
            new_root = TreeNode(postorder[postorder_left_flag + length - 1])
            new_root.left = self.build_binary_tree(inorder, inorder_left_flag, postorder, postorder_left_flag,
                                                   left_length)
            new_root.right = self.build_binary_tree(inorder, inorder_left_flag + 1 + left_length, postorder,
                                                    postorder_left_flag + left_length, length - left_length - 1)
            return new_root