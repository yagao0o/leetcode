# Author  :  Yagao0o
# Date    :  2015-01-23
# Source  :  https://oj.leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Given a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list.
#
# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        begin = ListNode(0)
        begin.next = head
        pre_node = begin
        current = head
        while current:
            is_duplicate = False
            current_value = current.val
            if current.next and current.next.val == current.val:
                    is_duplicate = True
            if is_duplicate:
                while current and current.val == current_value:
                    current = current.next
                pre_node.next = current
            elif current:
                pre_node = current
                current = current.next
        return begin.next