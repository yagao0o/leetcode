# Author  :  Yagao0o
# Date    :  2015-02-18
# Source  :  https://oj.leetcode.com/problems/gray-code/

# The gray code is a binary numeral system where two successive values differ in only one bit.
#
# Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code.
# A gray code sequence must begin with 0.
#
# For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:
#
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
# Note:
# For a given n, a gray code sequence is not uniquely defined.
#
# For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.
#
# For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.

class Solution:
    # @return a list of integers
    def grayCode(self, n):
        if n == 0:
            return
        result = [0, 1]
        current = 1
        current_size = 2
        while current < n:
            current += 1
            for i in range(current_size):
                result.append(result[current_size - 1 - i] + current_size)
            current_size <<= 1
        return result

a = Solution()
for i in range(5):
    print i
    print a.grayCode(i)
    print '----------'