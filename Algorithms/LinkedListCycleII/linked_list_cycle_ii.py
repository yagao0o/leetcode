# Author  :  Yagao0o
# Date    :  2015-06-03
# Source  :  https://leetcode.com/problems/linked-list-cycle-ii/

# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
# Follow up:
# Can you solve it without using extra space?

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head is None or head.next is None:
            return None
        slow, fast = head.next, head.next.next
        while slow != fast:
            if fast is None or fast.next is None:
                return None
            slow, fast = slow.next, fast.next.next
        while head != slow:
            print head.val, slow.val
            head, slow = head.next, slow.next
        return head