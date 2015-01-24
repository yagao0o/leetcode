# Author  :  Yagao0o
# Date    :  2014-11-16
# Source  :  https://oj.leetcode.com/problems/balanced-binary-tree/

# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as a binary tree in which
# the depth of the two subtrees of every node never differ by more than 1.


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        return self.judge_balance(root)[0]
    def judge_balance(self, root):
        if root is None:
            return True, 0
        left_balance, left_depth = self.judge_balance(root.left)
        right_balance, right_depth = self.judge_balance(root.right)
        if left_balance and right_balance:
            max_depth = max(left_depth, right_depth)
            if 2 * max_depth - left_depth - right_depth <= 1:
                return True, max_depth + 1
        return False, 0