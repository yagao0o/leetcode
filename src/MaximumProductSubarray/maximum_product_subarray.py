# Author  :  Yagao0o
# Date    :  2015-06-09
# Source  :  https://leetcode.com/problems/maximum-product-subarray/

# Find the contiguous subarray within an array (containing at least one number) which has the largest product.
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        max_num = nums[0]
        current_list = []
        for i in nums:
            max_num = max(max_num, i)
            if i == 0:
                if current_list:
                    max_num = max(max_num, self.count_max(current_list))
                    current_list = []
            else:
                current_list.append(i)
        if current_list:
            max_num = max(max_num, self.count_max(current_list))
        return max_num

    def count_max(self, n_list):
        if len(n_list) == 1:
            return n_list[0]
        total = 1
        nage_num = 0
        for n in n_list:
            total *= n
            if n < 0:
                nage_num += 1
        if nage_num % 2 == 0:
            return total
        else:
            left = 1
            for i in range(len(n_list)):
                left *= n_list[i]
                if n_list[i] < 0:
                    break
            right = 1
            for i in range(len(n_list)):
                right *= n_list[- i - 1]
                if n_list[- i - 1] < 0:
                    break
            return max(total/left, total/right)