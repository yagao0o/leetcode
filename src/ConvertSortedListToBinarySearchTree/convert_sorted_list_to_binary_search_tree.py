# Author  :  Yagao0o
# Date    :  2015-03-01
# Source  :  https://oj.leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        current, result = self.create_tree(head, length)
        return result

    def create_tree(self, head, length):
        # @param head, a list node, from where create binary tree
        # @param length, int, the nodes in the tree
        # @return current, a list node, next node to be dealt
        # @return new_root, the binary tree created
        if length == 0:
            return head, None
        elif length == 1:
            new_root = TreeNode(head.val)
            current = head.next
        else:
            new_root = TreeNode(0)
            current, left_child = self.create_tree(head, length / 2)
            new_root.val = current.val
            new_root.left = left_child
            current, right_child = self.create_tree(current.next, length - 1 - length / 2)
            new_root.right = right_child
        return current, new_root



