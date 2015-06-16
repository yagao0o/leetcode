# Author  :  Yagao0o
# Date    :  2015-06-16
# Source  :  https://leetcode.com/problems/count-primes/

# Description:
#
# Count the number of prime numbers less than a non-negative number, n.
#
# Credits:
# Special thanks to @mithmatt for adding this problem and creating all test cases.

class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        total = 0
        check_list = [1]*n
        for i in range(2,n):
            if check_list[i] == 1:
                total += 1
                current = i
                while current < n:
                    check_list[current], current = 0, current + i
        return total