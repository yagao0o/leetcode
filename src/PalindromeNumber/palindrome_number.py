# Author  :  Yagao0o
# Date    :  2014-11-4
# Source  :  https://oj.leetcode.com/problems/palindrome-number/

# Determine whether an integer is a palindrome. Do this without extra space.
#
# Some hints:
# Could negative integers be palindromes? (ie, -1)
#
# If you are thinking of converting the integer to string, note the restriction of using extra space.
#
# You could also try reversing an integer. However, if you have solved the problem "Reverse Integer",
# you know that the reversed integer might overflow. How would you handle such case?
#
# There is a more generic way of solving this problem.


class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        num_str = str(x)
        for i in range(len(num_str)/2 + 1):
            if num_str[i] != num_str[-i-1]:
                return False
        return True