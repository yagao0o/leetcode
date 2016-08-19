# Author  :  Yagao0o
# Date    :  2015-06-16
# Source  :  https://leetcode.com/problems/remove-linked-list-elements/

# Remove all elements from a linked list of integers that have value val.
#
# Example
# Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
# Return: 1 --> 2 --> 3 --> 4 --> 5
#
# Credits:
# Special thanks to @mithmatt for adding this problem and creating all test cases.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        left_flag = ListNode(0)
        left_flag.next = head
        last = left_flag
        current = head
        while current is not None:
            if current.val == val:
                last.next = current.next
            else:
                last = current
            current = last.next
        return left_flag.next