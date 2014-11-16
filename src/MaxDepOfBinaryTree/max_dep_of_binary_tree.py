# Author  :  Yagao0o
# Date    :  2014-11-16
# Source  :  https://oj.leetcode.com/problems/maximum-depth-of-binary-tree/

# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root is None:
            return 0
        depth = 0
        node_list = [root]
        while node_list:
            depth += 1
            child_list = []
            for node in node_list:
                if node.left is not None:
                    child_list.append(node.left)
                if node.right is not None:
                    child_list.append(node.right)
            node_list = child_list
        return depth

