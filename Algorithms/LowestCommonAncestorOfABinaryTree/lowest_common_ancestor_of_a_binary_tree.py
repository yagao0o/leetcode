# Author  :  Yagao0o
# Date    :  2015/9/2
# Source  :  https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
#
# According to the definition of LCA on Wikipedia:
# The lowest common ancestor is defined between two nodes v and w as the lowest node
# in T that has both v and w as descendants (where we allow a node to be a descendant of itself).
#
#         _______3______
#        /              \
#     ___5__          ___1__
#    /      \        /      \
#    6      _2       0       8
#          /  \
#          7   4
# For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5,
# since a node can be a descendant of itself according to the LCA definition.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        lowest_ancestor, p_in, q_in =  self.find_lowest_common_ancestor(root, p, q)
        return lowest_ancestor


    def find_lowest_common_ancestor(self, root, p, q):
        p_in = False
        q_in = False
        lowest_ancestor = None
        if root.left:
            lowest_ancestor_left, p_in_left, q_in_left = self.find_lowest_common_ancestor(root.left, p, q)
            p_in |= p_in_left
            q_in |= q_in_left
            lowest_ancestor = lowest_ancestor_left if lowest_ancestor_left else lowest_ancestor
        if lowest_ancestor is None and root.right:
            lowest_ancestor_right, p_in_right, q_in_right = self.find_lowest_common_ancestor(root.right, p, q)
            p_in |= p_in_right
            q_in |= q_in_right
            lowest_ancestor = lowest_ancestor_right if lowest_ancestor_right else lowest_ancestor
        if root == p:
            p_in = True
        if root == q:
            q_in = True
        if lowest_ancestor is None and p_in and q_in:
            lowest_ancestor = root
        return lowest_ancestor, p_in, q_in