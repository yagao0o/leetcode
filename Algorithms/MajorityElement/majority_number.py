# Author  :  Yagao0o
# Date    :  2015-01-24
# Source  :  https://oj.leetcode.com/problems/majority-element/

# Given an array of size n, find the majority element.
# The majority element is the element that appears more than  n/2  times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.
#
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.


class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        num = sorted(num)
        for i in range(len(num)/2 + 1):
            if num[i] == num[i + len(num) / 2]:
                return num[i]