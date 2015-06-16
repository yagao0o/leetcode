# Author  :  Yagao0o
# Date    :  2015-03-01
# Source  :  https://oj.leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Given a binary tree, return the zigzag level order traversal of its nodes' values.
# (ie, from left to right, then right to left for the next level and alternate between).
#
# For example:
# Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        result = []
        current = [root]
        in_order = True
        while current:
            new = []
            current_line = []
            if in_order:
                for current_node in current:
                    if current_node:
                        current_line.append(current_node.val)
                        new.append(current_node.left)
                        new.append(current_node.right)
            else:
                for current_node in range(len(current)-1, -1, -1):
                    if current[current_node]:
                        current_line.append(current[current_node].val)
                        new.insert(0, current[current_node].right)
                        new.insert(0, current[current_node].left)
            if current_line:
                result.append(current_line)
            in_order = not in_order
            current = new
        return result

