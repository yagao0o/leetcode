# Author  :  Yagao0o
# Date    :  2015-03-01
# Source  :  https://oj.leetcode.com/problems/flatten-binary-tree-to-linked-list/

# Given a binary tree, flatten it to a linked list in-place.
#
# For example,
# Given
#
#          1
#         / \
#        2   5
#       / \   \
#      3   4   6
# The flattened tree should look like:
#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6
#
# Hints:
# If you notice carefully in the flattened tree,
# each node's right child points to the next node of a pre-order traversal.

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if not root:
            return
        self.tree_flatten(root)


    def tree_flatten(self, root):
        left = root.left
        root.left = None
        right = root.right
        root.right = None
        last = root
        if left:
            last.right, last = self.tree_flatten(left)
        if right:
            last.right, last = self.tree_flatten(right)
        return root, last