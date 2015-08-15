# Author  :  Yagao0o
# Date    :  2015/8/15
# Source  :  https://leetcode.com/problems/palindrome-linked-list/

# Given a singly linked list, determine if it is a palindrome.
#
# Follow up:
# Could you do it in O(n) time and O(1) space?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        if length <= 1:
            return True
        left = None
        half = length / 2
        current = head
        for i in xrange(half):
            next = current.next
            current.next = left
            left = current
            current = next
        if length - half * 2 == 1:
            current = current.next
        for i in xrange(half):
            if current.val != left.val:
                return False
            current, left = current.next, left.next
        return True