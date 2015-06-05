# Author  :  Yagao0o
# Date    :  2015-06-05
# Source  :  https://leetcode.com/problems/reorder-list/

# Given a singly linked list L: L0->L1->...->Ln-1->Ln,
# reorder it to: L0->Ln->L1->Ln-1->L2->Ln-2->....
# You must do this in-place without altering the nodes' values.
# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {void} Do not return anything, modify head in-place instead.
    def reorderList(self, head):
        current = head
        length = 0
        while current:
            length += 1
            current = current.next
        if length <= 1:
            return head
        half = length / 2
        current = head
        while half > 0:
            current = current.next
            half -= 1
        right = self.reverse(current.next)
        current.next = None
        left = head.next
        current = head
        while left and right:
            current.next = right
            right = right.next
            current = current.next
            current.next = left
            left = left.next
            current = current.next

    def reverse(self, node):
        if node == None:
            return None
        head = node
        current = node.next
        head.next = None
        while current:
            next = current.next
            current.next = head
            head = current
            current = next
        return head