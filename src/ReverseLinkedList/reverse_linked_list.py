# Author  :  Yagao0o
# Date    :  2015-06-16
# Source  :  https://leetcode.com/problems/reverse-linked-list/

# Reverse a singly linked list.
#
# Hint:
# A linked list can be reversed either iteratively or recursively. Could you implement both?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        left_flag = ListNode(0)
        current = head
        while current:
            next = current.next
            current.next = left_flag.next
            left_flag.next = current
            current = next
        return left_flag.next

    def reverseList_rec(self, head):
        if head is None:
            return head
        head,tail = self.rec_reverse(head)
        tail.next = None
        return head

    def rec_reverse(self,head):
        if head.next is None:
            return head, head
        h, t = self.rec_reverse(head.next)
        t.next = head
        return h,head
