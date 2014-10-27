# Author  :  Yagao0o
# Date    :  2014-10-27
# Source  : https://oj.leetcode.com/problems/symmetric-tree/

# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3
# Note:
# Bonus points if you could solve it both recursively and iteratively.
#
# confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
#
#
# OJ's Binary Tree Serialization:
# The serialization of a binary tree follows a level order traversal,
# where '#' signifies a path terminator where no node exists below.
#
# Here's an example:
#    1
#   / \
#  2   3
#     /
#    4
#     \
#      5
# The above binary tree is serialized as "{1,2,3,#,#,4,#,#,5}".


# Definition for a  binary tree node
#class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @return a boolean
    def __init__(self):
        pass

    def is_symmetric(self, root):
        if root is None:
            return True
        child_list = [root.left, root.right]
        return self.check_symmetric(child_list)

    def check_symmetric(self, child_list):
        length = len(child_list)
        if length == 0:
            return True
        elif length % 2 == 1:
            return False
        value_list = []
        reverse_value = []
        new_child_list = []
        for number in range(length):
            current_node = child_list[number]
            if current_node is None:
                value_list.append('#')
                reverse_value.insert(0, '#')
            else:
                value_list.append(current_node.val)
                reverse_value.insert(0, current_node.val)
                new_child_list.append(current_node.left)
                new_child_list.append(current_node.right)
        for number in range(length):
            if value_list[number] != reverse_value[number]:
                return False
        return self.check_symmetric(new_child_list)
