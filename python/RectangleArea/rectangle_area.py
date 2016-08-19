# Author  :  Yagao0o
# Date    :  2015/6/23
# Source  :  https://leetcode.com/problems/rectangle-area/

# Find the total area covered by two rectilinear rectangles in a 2D plane.
#
# Each rectangle is defined by its bottom left corner and top right corner [as shown in the figure].
#
# Assume that the total area is never beyond the maximum possible value of int.
#
# Credits:
# Special thanks to @mithmatt for adding this problem, creating the above image and all test cases.


class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        x = [A, C, E, G]
        x.sort()
        y = [B, D, F, H]
        y.sort()
        size =  (C - A) * (D - B) + (G - E) * (H - F)
        if (E > C or A > G) or (F > D or B > H):
            return size
        return size - (x[2] - x[1]) * (y[2] - y[1])