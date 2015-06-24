# Author  :  Yagao0o
# Date    :  2015/6/24
# Source  :  https://leetcode.com/problems/invert-binary-tree/

# Invert a binary tree.
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# to
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
# Trivia:
# This problem was inspired by this original tweet by Max Howell:
#   Google: 90% of our engineers use the software you wrote (Homebrew),
#   but you can't invert a binary tree on a whiteboard so fuck off.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if root is None:
            return root
        left = self.invertTree(root.right)
        right = self.invertTree(root.left)
        root.left, root.right = left, right
        return root

# I think google should hire me for passing it by one submission.