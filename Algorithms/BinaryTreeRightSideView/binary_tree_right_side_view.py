# Author  :  Yagao0o
# Date    :  2015-06-14
# Source  :  https://leetcode.com/problems/binary-tree-right-side-view/

# Given a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.
#
# For example:
# Given the following binary tree,
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---
# You should return [1, 3, 4].
#
# Credits:
# Special thanks to @amrsaqr for adding this problem and creating all test cases.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def rightSideView(self, root):
        result = []
        current_list = []
        if root is not None:
            current_list.append(root)
        while current_list:
            result.append(current_list[-1].val)
            next_list = []
            for node in current_list:
                if node.left is not None:
                    next_list.append(node.left)
                if node.right is not None:
                    next_list.append(node.right)
            current_list  = next_list
        return result
