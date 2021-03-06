# Author  :  Yagao0o
# Date    :  2015-01-23
# Source  :  https://oj.leetcode.com/problems/remove-duplicates-from-sorted-list/

# Given a sorted linked list, delete all duplicates such that each element appear only once.
#
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        current = head
        while current:
            if current.next and current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
