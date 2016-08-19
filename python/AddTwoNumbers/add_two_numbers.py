# Author  :  Yagao0o
# Date    :  2015-01-26
# Source  :  https://oj.leetcode.com/problems/add-two-numbers/


# You are given two linked lists representing two non-negative numbers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        carry = 0
        head = ListNode(0)
        current = head
        while l1 and l2:
            new_carry = (l1.val + l2.val + carry) / 10
            current.next = ListNode(l1.val + l2.val + carry - 10 * new_carry)
            current = current.next
            l1 = l1.next
            l2 = l2.next
            carry = new_carry
        if l1:
            left = l1
        else:
            left = l2
        while left:
            if carry == 0:
                current.next = left
                left = None
            else:
                new_carry = (left.val + carry) / 10
                current.next = ListNode(left.val + carry - 10 * new_carry)
                current = current.next
                left = left.next
                carry = new_carry
        if carry == 1:
            current.next = ListNode(1)
        return head.next

def travel(node):
    while node:
        print node.val
        node = node.next

a1 = ListNode(1)
# a2 = ListNode(8)
# a3 = ListNode(9)
# a1.next = a2
# a2.next = a3

b1 = ListNode(9)
b2 = ListNode(9)
# b3 = ListNode(1)
b1.next = b2
# b2.next = b3

AA = Solution()
result = AA.addTwoNumbers(a1, b1)
travel(result)



