# Author  :  Yagao0o
# Date    :  2015-01-23
# Source  :  https://oj.leetcode.com/problems/climbing-stairs/


# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n <= 2:
            return n
        before_stair = 1
        current_stair = 2
        for k in range(2, n):
            new_stair = before_stair + current_stair
            before_stair = current_stair
            current_stair = new_stair
        return current_stair


