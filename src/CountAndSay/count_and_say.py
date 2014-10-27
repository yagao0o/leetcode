# Author  :  Yagao0o
# Date    :  2014-10-27
# Source  :  https://oj.leetcode.com/problems/count-and-say/

# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...
#
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth sequence.
#
# Note: The sequence of integers will be represented as a string.


class Solution:
    # @return a string
    def countAndSay(self, n):
        if n == 0:
            return ""
        result = "1"
        count = 1
        while count < n:
            result = self.say(result)
            count = count + 1
        return result

    def say(self, numbers):
        result = ""
        last = ""
        count = 0
        for no in range(len(numbers)):
            if numbers[no] != last:
                if last and count > 0:
                    result = result + str(count) + last
                last = numbers[no]
                count = 1
            else:
                count += 1
        if last and count > 0:
                    result = result + str(count) + last
        return result


