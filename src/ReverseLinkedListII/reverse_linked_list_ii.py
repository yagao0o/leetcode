# Author  :  Yagao0o
# Date    :  2015-02-
# Source  :  https://oj.leetcode.com/problems/reverse-linked-list-ii/

# Reverse a linked list from position m to n. Do it in-place and in one-pass.
#
# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,
#
# return 1->4->3->2->5->NULL.
#
# Note:
# Given m, n satisfy the following condition:
# 1 <= m <= n <= length of list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        left_flag = ListNode(0)
        left_flag.next = head
        current = head
        last = left_flag
        count = 0
        while current:
            count += 1
            if count == m:
                cut_point = last
                reverse_part_last = current
                reverse_part_left = current
                current = current.next
            elif m < count < n:
                last = current.next
                current.next = reverse_part_left
                reverse_part_left = current
                current = last
            elif count == n:
                last = current.next
                cut_point.next = current
                current.next = reverse_part_left
                reverse_part_last.next = last
            elif count > n:
                break
            else:
                last = current
                current = current.next
        return left_flag.next

def travel(node):
    while node:
        print node.val,
        node = node.next
    print
a = Solution()
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

travel(n1)
travel(a.reverseBetween(n1,1,5))