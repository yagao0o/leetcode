# Author  :  Yagao0o
# Date    :  2015-02-19
# Source  :  https://oj.leetcode.com/problems/restore-ip-addresses/

# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
#
# For example:
# Given "25525511135",
#
# return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

#yagao note:not a good idea, but maybe efficient LOL

class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        result = []
        for part_one in range(1,4):
            for part_two in range(1,4):
                for part_three in range(1,4):
                    part_four = len(s) - part_one - part_two - part_three
                    if part_four < 1 or part_four > 3:
                        continue
                    part_one_int = s[0:part_one]
                    part_two_int = s[part_one: part_one + part_two]
                    part_three_int = s[part_one + part_two: part_one + part_two + part_three]
                    part_four_int = s[part_one + part_two + part_three:]
                    if part_one > 1 and part_one_int[0] == '0':
                        continue
                    if part_two > 1 and part_two_int[0] == '0':
                        continue
                    if part_three > 1 and part_three_int[0] == '0':
                        continue
                    if part_four > 1 and part_four_int[0] == '0':
                        continue
                    if 0 <= int(part_one_int) <= 255 and 0 <= int(part_two_int) <= 255 and \
                                            0 <= int(part_three_int) <= 255 and 0 <= int(part_four_int) <= 255:
                        result.append(part_one_int + '.' + part_two_int + '.' + part_three_int + '.' + part_four_int)
        return result
