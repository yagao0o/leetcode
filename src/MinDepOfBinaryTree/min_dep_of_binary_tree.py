# Author  :  Yagao0o
# Date    :  2014-11-16
# Source  :  https://oj.leetcode.com/problems/minimum-depth-of-binary-tree/

# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root is None:
            return 0
        node_list = [root]
        depth = 1
        while True:
            new_list = []
            for node in node_list:
                if node.left is None and node.right is None:
                    return depth
                if node.left is not None:
                    new_list.append(node.left)
                if node.right is not None:
                    new_list.append(node.right)
            node_list = new_list
            depth += 1
        return 0

