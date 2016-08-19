# Author  :  Yagao0o
# Date    :  2015-06-01
# Source  :  https://leetcode.com/problems/single-number-ii/

# Given an array of integers, every element appears three times except for one. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        binary_list = [0]
        is_negative = 0
        for num in nums:
            if num < 0 :
                is_negative += 1
                num = -num
            counter = 0
            while num > 0:
                current = num % 2
                num >>= 1
                if len(binary_list) < counter + 1:
                    binary_list.append(current)
                else:
                    binary_list[counter] += current
                counter += 1
        result = 0
        counter = 1
        for i in range(len(binary_list)):
            result += counter * (binary_list[i] % 3)
            counter <<= 1
        return result if is_negative % 3 == 0 else -result

n = [-2,-2,1,1,-3,1,-3,-3,-4,-2]
# n = [7,7,7,1]
a = Solution()
print a.singleNumber(n)