# Author  :  Yagao0o
# Date    :  2015-02-
# Source  :  https://oj.leetcode.com/problems/unique-binary-search-trees/

# Given n, how many structurally unique BST's (binary search trees) that store values 1...n?
#
# For example,
# Given n = 3, there are a total of 5 unique BST's.
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

class Solution:
    # @return an integer
    def numTrees(self, n):
        result = [1]
        for i in range(1, n + 1):
            a_i = 0
            left = 0
            right = i - 1
            while left < right:
                a_i += 2 * result[left] * result[right]
                left += 1
                right -= 1
            if left == right:
                a_i += result[left] * result[left]
            result.append(a_i)
        return result[n]

a = Solution()
for i in range(11):
    print a.numTrees(i)
