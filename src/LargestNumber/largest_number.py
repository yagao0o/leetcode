# Author  :  Yagao0o
# Date    :  2015-06-14
# Source  :  https://leetcode.com/problems/largest-number/

# Given a list of non negative integers, arrange them such that they form the largest number.
#
# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
#
# Note: The result may be very large, so you need to return a string instead of an integer.
#
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.

class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        str_list = []
        for num in nums:
            self.insert(str_list, num)
        while len(str_list) > 1 and int(str_list[0]) == 0:
            str_list.pop(0)
        return ''.join(str_list)

    def insert(self, str_list, new_number):
        new_str = str(new_number)
        i = 0
        while i < len(str_list):
            if not self.bigger_than(str_list[i], new_str):
                break
            i += 1
        str_list.insert(i, new_str)

    def bigger_than(self, num1, num2):
        l1 = len(num1)
        l2 = len(num2)
        for i in range(min(l1, l2)):
            if num1[i] > num2[i]:
                return True
            elif num1[i] < num2[i]:
                return False
        if l1 == l2:
            return False
        elif l1 < l2:
            return self.bigger_than(num1, num2[l1:])
        return self.bigger_than(num1[l2:],num2)