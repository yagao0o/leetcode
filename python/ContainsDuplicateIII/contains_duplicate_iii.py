# Author  :  Yagao0o
# Date    :  2015/6/17
# Source  :  https://leetcode.com/problems/contains-duplicate-iii/

# Given an array of integers, find out whether there are two distinct indices i and j in the array
# such that the difference between nums[i] and nums[j] is at most t and the difference between i and j is at most k.

# explain by yagao0o: Find if exist an pair i , j,which |i - j| < k and , |n[i] - n[j]| < t
# In the beginning , I use a sorted_list to store the k number in range, the insert and remove need O(logK)
# and the total complexity is O(NlogK) N is the length of nums
# but still TLE
# now the main idea from https://leetcode.com/discuss/38176/python-ordereddict, used a ordeded dictionary,and
# shrink the size by t, so only compare the key nearby. awesome idea!

import collections

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k == 0 or t < 0:
            return False
        dic = collections.OrderedDict()
        for num in nums:
            key = num if t == 0 else num // t
            for nearby in (dic.get(key - 1), dic.get(key), dic.get(key + 1)):
                if nearby is not None and abs(num - nearby) <= t:
                    return True
            if len(dic) == k:
                dic.popitem(False)
            dic[key] = num
        return False

    def containsNearbyAlmostDuplicate_2(self, nums, k, t):
        if k == 0:
            return False
        sorted_ls = []
        if k >= len(nums):
            for i in nums:
                new_idx = self.insert(sorted_ls, i)
                if self.judge_if_in_range(sorted_ls, new_idx, t):
                    return True
            return False
        for i in range(k + 1):
            new_idx = self.insert(sorted_ls, nums[i])
            if self.judge_if_in_range(sorted_ls, new_idx, t):
                return True
        for i in range(k + 1, len(nums)):
            sorted_ls.remove(nums[i - k - 1])
            new_idx = self.insert(sorted_ls, nums[i])
            if self.judge_if_in_range(sorted_ls, new_idx, t):
                return True
        return False

    def judge_if_in_range(self, sorted_list, idx, t):
        if idx == -1:
            if len(sorted_list) > 1 and abs(sorted_list[-1] - sorted_list[-2]) <= t:
                return True
        elif idx == 0:
            if len(sorted_list) > 1 and abs(sorted_list[0] - sorted_list[1]) <= t:
                return  True
        elif abs(sorted_list[idx - 1] - sorted_list[idx]) <= t or abs(sorted_list[idx] - sorted_list[idx + 1]) <= t:
            return True
        return False

    def insert(self, sorted_list, number):
        if not sorted_list or number >= sorted_list[-1]:
            sorted_list.append(number)
            return -1
        elif number <= sorted_list[0]:
            sorted_list.insert(0, number)
            return 0
        left = 0
        right = len(sorted_list) - 1
        while left != right:
            middle = (left + right) / 2
            if sorted_list[middle] > number:
                right = middle
            else:
                left = middle + 1
            sorted_list.insert(left, number)
            return left