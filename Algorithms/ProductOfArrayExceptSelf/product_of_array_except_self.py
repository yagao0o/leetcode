# Author  :  Yagao0o
# Date    :  2015/9/2
# Source  :  https://leetcode.com/problems/product-of-array-except-self/


# Given an array of n integers where n > 1, nums,
# return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
#
# Solve it without division and in O(n).
#
# For example, given [1,2,3,4], return [24,12,8,6].
#
# Follow up:
# Could you solve it with constant space complexity?
# (Note: The output array does not count as extra space for the purpose of space complexity analysis.)

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        all_product = 1
        num_of_zero = 0
        for i in nums:
            if i == 0:
                num_of_zero += 1
                if num_of_zero > 1:
                    return [0 for x in nums]
            else:
                all_product *= i
        if num_of_zero == 0:
            return [self.divide(all_product, x) for x in nums]
        else:
            return [0 if x !=0 else all_product for x in nums]

    def divide(self, divider, n):
        divider, is_nage = abs(divider), divider < 0
        n, is_nage = abs(n), is_nage != (n < 0)
        if n == 1:
            return -divider if is_nage else divider
        result = 0
        while divider >= n:
            n2 = n
            k = 1
            while divider >= n2:
                k <<= 1
                n2 <<= 1
            result += k >> 1
            divider -= n2 >> 1
        return -result if is_nage else result