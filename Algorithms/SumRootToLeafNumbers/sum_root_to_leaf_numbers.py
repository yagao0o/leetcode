# Author  :  Yagao0o
# Date    :  2015-05-25
# Source  :  https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
#
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
#
# Find the total sum of all root-to-leaf numbers.
#
# For example,
#
#     1
#    / \
#   2   3
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
#
# Return the sum = 12 + 13 = 25.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def sumNumbers(self, root):
        result = 0
        if not root:
            return result
        current_nodes = [root]
        current_nodes_amount = [root.val]
        while current_nodes:
            current = current_nodes.pop(0)
            current_amount = current_nodes_amount.pop(0)
            if not current.left and not current.right:
                result += current_amount
            else:
                if current.left:
                    current_nodes.append(current.left)
                    current_nodes_amount.append(current_amount * 10 + current.left.val)
                if current.right:
                    current_nodes.append(current.right)
                    current_nodes_amount.append(current_amount * 10 + current.right.val)
        return result