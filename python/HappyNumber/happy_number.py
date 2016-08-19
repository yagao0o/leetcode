# Author  :  Yagao0o
# Date    :  2015-06-16
# Source  :  https://leetcode.com/problems/happy-number/

# Write an algorithm to determine if a number is "happy".
#
# A happy number is a number defined by the following process: Starting with any positive integer,
#  replace the number by the sum of the squares of its digits,
# and repeat the process until the number equals 1 (where it will stay),
#  or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy numbers.
#
# Example: 19 is a happy number
#
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
# Credits:
# Special thanks to @mithmatt and @ts for adding this problem and creating all test cases.

class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        travelled = []
        current_list = self.get_number_list(n)
        travelled.append(n)
        while len(current_list) > 1 or current_list[0] != 1:
            new_number = 0
            for i in current_list:
                new_number += i * i
            if new_number in travelled:
                return False
            current_list = self.get_number_list(new_number)
            travelled.append(new_number)
        return True

    def get_number_list(self, n):
        result = []
        while n > 0:
            result.append(n % 10)
            n = n / 10
        return result