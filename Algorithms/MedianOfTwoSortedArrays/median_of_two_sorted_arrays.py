# Author  :  Yagao0o
# Date    :  2015/9/15
# Source  :  https://leetcode.com/problems/median-of-two-sorted-arrays/

# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len_1 = len(nums1)
        len_2 = len(nums2)
        if len_1 > len_2:
            nums1, nums2, len_1, len_2 = nums2, nums1, len_2, len_1
        left, right, left_total = 0, len_1, (len_1 + len_2 + 1) / 2
        while left <= right:
            middle = (left + right) / 2
            middle2 = left_total - middle
            if middle2 > 0 and middle < len_1 and nums2[middle2 - 1] > nums1[middle]:
                left = middle + 1
            elif middle > 0 and middle2 < len_2 and nums1[middle - 1] > nums2[middle2]:
                right = middle - 1
            else:
                if middle == 0:
                    number1 = nums2[middle2 - 1]
                elif middle2 == 0:
                    number1 = nums1[middle - 1]
                else:
                    number1 = max(nums1[middle - 1], nums2[middle2 - 1])
                if (len_1 + len_2) % 2 == 1:
                    return number1
                if middle == len_1:
                    number2 = nums2[middle2]
                elif middle2 == len_2:
                    number2 = nums1[middle]
                else:
                    print middle, middle2
                    number2 = min(nums1[middle], nums2[middle2])
                print number1, number2
                return (number1 + number2) / 2.0