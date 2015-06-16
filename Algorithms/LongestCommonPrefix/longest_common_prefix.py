# Author  :  Yagao0o
# Date    :  2014-11-10
# Source  :  https://oj.leetcode.com/problems/min-stack/

# Write a function to find the longest common prefix string amongst an array of strings.

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if strs:
            common_prefix = strs[0]
            for string in strs:
                common_prefix = self.get_common_prefix(common_prefix, string)
            return common_prefix
        return ""

    def get_common_prefix(self, str_a, str_b):
        result = ""
        i = 0
        while i < len(str_a) and i < len(str_b):
            if str_a[i] == str_b[i]:
                result += str_a[i]
            else:
                return result
            i += 1
        return result