# Author  :  Yagao0o
# Date    :  2015-01-23
# Source  :  https://oj.leetcode.com/problems/intersection-of-two-linked-lists/

# Write a program to find the node at which the intersection of two singly linked lists begins.
#
#
# For example, the following two linked lists:
#
# A:          a1 -> a2
#                      \
#                       c1 -> c2 ->c3
#                      /
# B:     b1 -> b2 -> b3
# begin to intersect at node c1.
#
#
# Notes:
#
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.
# Credits:
# Special thanks to @stellari for adding this problem and creating all test cases.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        a_list = []
        b_list = []
        len_a = 0
        len_b = 0
        current_a = headA
        while current_a:
            len_a += 1
            a_list.append(current_a)
            current_a = current_a.next
        current_b = headB
        while current_b:
            len_b += 1
            b_list.append(current_b)
            current_b = current_b.next
        intersection_node = None
        for i in range(min(len_a, len_b)):
            if a_list[len_a - i -1] == b_list[len_b - i - 1]:
                intersection_node = a_list[len_a - i -1]
            else:
                break
        return intersection_node