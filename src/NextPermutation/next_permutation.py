# Author  :  Yagao0o
# Date    :  2015-02-05
# Source  :  https://oj.leetcode.com/problems/next-permutation/

# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
#
# If such arrangement is not possible,
# it must rearrange it as the lowest possible order (ie, sorted in ascending order).
#
# The replacement must be in-place, do not allocate extra memory.
#
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 -> 1,3,2
# 3,2,1 -> 1,2,3
# 1,1,5 -> 1,5,1

class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        length = len(num)
        if length <= 1:
            return num
        for i in range(1, length):
            if num[length - 1 - i] < num[length - 1]:
                #Find the changed number and change
                current_position = length - i
                while num[current_position] <= num[length - 1 - i]:
                    current_position += 1
                temp = num[length - 1 - i]
                num[length - 1 - i] = num[current_position]
                num[current_position] = temp
                break
            else:
                current_position = length - 1 - i
                temp = num[current_position]
                while current_position < length - 1:
                    num[current_position] = num[current_position + 1]
                    current_position += 1
                num[length - 1] = temp
        return num

#to be optimize
#find the first i which a(i) < a(i + 1)
#an sort a(i + 1) - a(n) by merge sort
#then change the a(i) with the a(j) which a(j - 1) <= a(i) and a(j) > a(i)
