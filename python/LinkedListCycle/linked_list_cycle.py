# Author  :  Yagao0o
# Date    :  2015-06-03
# Source  :  https://leetcode.com/problems/linked-list-cycle/

# Given a linked list, determine if it has a cycle in it.
# Follow up:
# Can you solve it without using extra space?

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        current = head
        while current:
            if current.next == current:
                return True
            next = current.next
            current.next = current
            current = next
        return False