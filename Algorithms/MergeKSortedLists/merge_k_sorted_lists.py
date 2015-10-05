# Author  :  Yagao0o
# Date    :  2015/10/5
# Source  :  https://leetcode.com/problems/merge-k-sorted-lists/


# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        sorted_lists = []
        for new_list in lists:
            if new_list:
                self.insert_to_list(sorted_lists, new_list)

        head = ListNode(0)
        current = head
        while sorted_lists:
            head_list = sorted_lists.pop(0)
            current.next, current, head_list = head_list, head_list, head_list.next
            if head_list:
                self.insert_to_list(sorted_lists, head_list)
        return head.next

    def insert_to_list(self, sorted_lists, new_list):
        if not sorted_lists:
            sorted_lists.append(new_list)
            return
        left = 0
        right = len(sorted_lists) - 1
        if new_list.val < sorted_lists[0].val:
            sorted_lists.insert(0, new_list)
        elif new_list.val > sorted_lists[right].val:
            sorted_lists.append(new_list)
        else:
            while left < right:
                middle = (left + right) / 2
                if sorted_lists[middle].val == new_list.val:
                    left, right = middle, middle
                elif sorted_lists[middle].val < new_list.val:
                    left = middle + 1
                else:
                    right = middle
            sorted_lists.insert(left, new_list)
        return


