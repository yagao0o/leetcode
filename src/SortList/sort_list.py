# Author  :  Yagao0o
# Date    :  2015-06-08
# Source  :  https://leetcode.com/problems/sort-list/

# Sort a linked list in O(n log n) time using constant space complexity.
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def sortList(self, head):
        if head is None:
            return None
        length = 0
        current = head
        while current:
            length, current = length + 1, current.next
        return self.merge_sort(head, length)

    def merge_sort(self, head, length):
        if length == 1:
            return head
        # split into two list
        left_length = length / 2
        right_length = length - left_length
        left_head = left_tail = right_head = head
        for i in range(left_length):
            left_tail = right_head
            right_head = right_head.next
        left_tail.next = None
        # sort list
        left_head = self.merge_sort(left_head, left_length)
        right_head = self.merge_sort(right_head, right_length)
        # merge list
        total_head = ListNode(None)
        current = total_head
        while left_head and right_head:
            if left_head.val < right_head.val:
                current.next, left_head = left_head, left_head.next
            else:
                current.next, right_head = right_head, right_head.next
            current = current.next
        if left_head:
            current.next = left_head
        else:
            current.next = right_head
        return total_head.next
