# Author  :  Yagao0o
# Date    :  2015-06-05
# Source  :  https://leetcode.com/problems/binary-tree-preorder-traversal/

# Given a binary tree, return the preorder traversal of its nodes' values.
# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [1,2,3].
#
# Note: Recursive solution is trivial, could you do it iteratively

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def preorderTraversal(self, root):
        result = []
        if root is None:
            return result
        current = [root]
        while current:
            node = current.pop(0)
            result.append(node.val)
            if node.right:
                current.insert(0, node.right)
            if node.left:
                current.insert(0, node.left)
        return result