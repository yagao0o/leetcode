# Author  :  Yagao0o
# Date    :  2015-06-14
# Source  :  https://leetcode.com/problems/rotate-array/

# Rotate an array of n elements to the right by k steps.
#
# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
#
# Note:
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
#
# Hint:
# Could you do it in-place with O(1) extra space?
# Related problem: Reverse Words in a String II
#
# Credits:
# Special thanks to @Freezen for adding this problem and creating all test cases.

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        cp = nums[:]
        l = len(nums)
        for i in range(l):
            nums[i] = cp[(i + l - k) % l]

    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate2(self, nums, k):
        #this method used O(1) extra space
        if k == 0:
            return
        l = len(nums)
        aa = l
        b = k
        while aa % b != 0:
            aa, b = b, aa % b
        for i in range(b):
            current = i
            tmp = nums[current]
            while True:
                current = current + k
                if current >= l:
                    current %= l
                nums[current], tmp = tmp, nums[current]
                if current == i:
                    break