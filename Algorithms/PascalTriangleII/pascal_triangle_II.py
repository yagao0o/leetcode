# Author  :  Yagao0o
# Date    :  2014-11-10
# Source  :  https://oj.leetcode.com/problems/pascals-triangle-ii/

# Given an index k, return the kth row of the Pascal's triangle.
#
# For example, given k = 3,
# Return [1,3,3,1].
#
# Note:
# Could you optimize your algorithm to use only O(k) extra space?

class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        result = []
        for row in range(rowIndex + 1):
            if row == 0:
                result.append(1)
            elif row == 1:
                result.append(1)
            else:
                result.insert(0, 1)
                for number in range(1, row):
                    result[number] = result[number] + result[number + 1]
        return result