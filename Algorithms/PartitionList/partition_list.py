# Author  :  Yagao0o
# Date    :  2015-02-17
# Source  :  https://oj.leetcode.com/problems/partition-list/

# Given a linked list and a value x,
# partition it such that all nodes less than x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the two partitions.
#
# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        left = None
        left_current = None
        right = None
        right_current = None
        current = head
        while current is not None:
            if current.val < x:
                if left_current is None:
                    left = current
                    left_current = current
                else:
                    left_current.next = current
                    left_current = left_current.next
            else:
                if right_current is None:
                    right = current
                    right_current = current
                else:
                    right_current.next = current
                    right_current = right_current.next
            current = current.next
        if right_current is not None:
            right_current.next = None
        if left == None:
            return right
        else:
            left_current.next = right
            return left