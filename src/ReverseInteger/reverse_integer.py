# Author  :  Yagao0o
# Date    :  2014-10-27
# Source  :  https://oj.leetcode.com/problems/reverse-integer/

# Reverse digits of an integer.
#
# Example1: x = 123, return 321
# Example2: x = -123, return -321
#
# click to show spoilers.
#
# Have you thought about this?
# Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!
#
# If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.
#
# Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer,
#       then the reverse of 1000000003 overflows. How should you handle such cases?
#
# Throw an exception? Good, but what if throwing an exception is not an option?
#       You would then have to re-design the function (ie, add an extra parameter).


#TODO Unsolved leetcode.com Show Compile Error


class Solution:
    # @return an integer
    def reverse(self, x):
        number_string = str(x)
        result_string = []
        if number_string[0] == '-':
            result_string.append('-')
            number_string = number_string[1:]
        is_start = True
        for count in range(len(number_string)):
            char = number_string[len(number_string) - 1 - count]
            if not(char == '0' and is_start):
                result_string.append(char)
                is_start = False
        result = eval(''.join(result_string))
        return result

a = Solution()
print a.reverse(123)
print a.reverse(745)
print a.reverse(-123.1600)
print a.reverse( -122025)
