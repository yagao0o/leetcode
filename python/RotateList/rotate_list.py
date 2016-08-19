# Author  :  Yagao0o
# Date    :  2015-02-13
# Source  :  https://oj.leetcode.com/problems/rotate-list/

# Given a list, rotate the list to the right by k places, where k is non-negative.
#
# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if not head or k == 0:
            return head
        left = ListNode(0)
        left.next = head
        current = head
        length = 1
        cut_point = None
        while current.next:
            current = current.next
            length += 1
            if cut_point:
                cut_point = cut_point.next
            elif length > k:
                cut_point = head
        if cut_point:
            current.next = head
            left.next = cut_point.next
            cut_point.next = None
            return left.next
        else:
            return self.rotateRight(head, k % length)
