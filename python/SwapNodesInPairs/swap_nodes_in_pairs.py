# Author  :  Yagao0o
# Date    :  2015-02-04
# Source  :  https://oj.leetcode.com/problems/swap-nodes-in-pairs/

# Given a linked list, swap every two adjacent nodes and return its head.
#
# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
# Your algorithm should use only constant space.
# You may not modify the values in the list, only nodes itself can be changed.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        left_flag = ListNode(0)
        left_flag.next = head
        current_last = left_flag
        while current_last:
            if current_last.next is None or current_last.next.next is None:
                break
            else:
                temp_node = current_last.next.next
                current_last.next.next = temp_node.next
                temp_node.next = current_last.next
                current_last.next = temp_node
                current_last = temp_node.next
        return left_flag.next