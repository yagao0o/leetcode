# Author  :  Yagao0o
# Date    :  2015-01-06
# Source  :  https://oj.leetcode.com/problems/remove-nth-node-from-end-of-list/

# Given a linked list, remove the nth node from the end of list and return its head.
#
# For example,
#
#    Given linked list: 1->2->3->4->5, and n = 2.
#
#    After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
# Given n will always be valid.
# Try to do this in one pass.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        result, postion  = self.removeFromEnd(head, n)
        return result

    def removeFromEnd(self, head, n):
        if head is None:
            return None,0
        child, position = self.removeFromEnd(head.next, n)
        head.next = child
        if position + 1 == n:
            return child, position + 1
        else:
            return head, position + 1
