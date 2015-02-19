# Author  :  Yagao0o
# Date    :  2015-02-
# Source  :  https://oj.leetcode.com/problems/binary-tree-inorder-traversal/

# Given a binary tree, return the inorder traversal of its nodes' values.
#
# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [1,3,2].
#
# Note: Recursive solution is trivial, could you do it iteratively?

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        if not root:
            return []
        return self.inorder_traversal(root)

    def inorder_traversal(self, node):
        result = []
        if node.left:
            result += self.inorder_traversal(node.left)
        result += [node.val]
        if node.right:
            result += self.inorder_traversal(node.right)
        return result


a = Solution()
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
# n1.right = n2
# n2.left = n3
print a.inorderTraversal(None)