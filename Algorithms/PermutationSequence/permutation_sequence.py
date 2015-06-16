# Author  :  Yagao0o
# Date    :  2015-02-12
# Source  :  https://oj.leetcode.com/problems/permutation-sequence/

# The set [1,2,3 ... n] contains a total of n! unique permutations.
#
# By listing and labeling all of the permutations in order,
# We get the following sequence (ie, for n = 3):
#
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.
#
# Note: Given n will be between 1 and 9 inclusive.

class Solution:
    # @return a string
    def getPermutation(self, n, k):
        number_list = []
        factorial = []
        result = ""
        for i in range(n):
            if i == 0:
                factorial.append(1)
            else:
                factorial.append(factorial[i - 1] * i)
            number_list.append(i + 1)
        for i in range(n - 1, 0, -1):
            current_positon = 0
            while k > factorial[i] and current_positon < i:
                current_positon += 1
                k -= factorial[i]
            result += str(number_list.pop(current_positon))
        result += str(number_list[0])
        return result