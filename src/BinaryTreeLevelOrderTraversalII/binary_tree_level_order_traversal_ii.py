# Author  :  Yagao0o
# Date    :  2015-01-23
# Source  :  https://oj.leetcode.com/problems/binary-tree-level-order-traversal/


# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (
#       ie, from left to right, level by level from leaf to root).
#
# For example:
# Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        result =[]
        current_nodes = []
        current_values = []
        if root:
            current_nodes = [root]
        while current_nodes:
            next_nodes = []
            current_values = []
            for node in current_nodes:
                if node:
                    current_values.append(node.val)
                    next_nodes.append(node.left)
                    next_nodes.append(node.right)
            if current_values:
                result.insert(0, current_values)
            current_nodes = next_nodes
        return result