# Author  :  Yagao0o
# Date    :  2015/6/23
# Source  :  https://leetcode.com/problems/count-complete-tree-nodes/

# Given a complete binary tree, count the number of nodes.
#
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last,
# is completely filled, and all nodes in the last level are as far left as possible.
# It can have between 1 and 2h nodes inclusive at the last level h.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        result,is_full =  self.count(root, None, None)
        return result

    def count(self, root, left_depth, right_depth):
        if root is None:
            return 0, True
        if left_depth is None:
            left_depth = 1
            left = root.left
            while left:
                left, left_depth = left.left, left_depth + 1
        if right_depth is None:
            right_depth = 1
            right = root.right
            while right:
                right, right_depth = right.right, right_depth + 1
        if left_depth == right_depth:
            return (1 << left_depth) - 1, True
        else:
            left_count, is_left_full = self.count(root.left, left_depth - 1, None)
            if is_left_full:
                right_count, is_right_full = self.count(root.right, None, right_depth - 1)
                return 1 + left_count + right_count, False
            else:
                return left_count + (1 << right_depth - 1), False
