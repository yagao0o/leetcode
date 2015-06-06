# Author  :  Yagao0o
# Date    :  2015-06-06
# Source  :  https://leetcode.com/problems/insertion-sort-list/

# Sort a linked list using insertion sort.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def insertionSortList(self, head):
        if head is None:
            return head
        left_flag = ListNode(None)
        current = head
        while current:
            next = current.next
            last = left_flag
            flag = last.next
            while flag is not None and flag.val < current.val:
                last = flag
                flag = last.next
            last.next = current
            current.next = flag
            current = next
        return left_flag.next