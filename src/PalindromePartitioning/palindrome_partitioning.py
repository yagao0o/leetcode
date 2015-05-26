# Author  :  Yagao0o
# Date    :  2015-05-26
# Source  :  https://leetcode.com/problems/palindrome-partitioning/


# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return all possible palindrome partitioning of s.
#
# For example, given s = "aab",
# Return
#
#   [
#     ["aa","b"],
#     ["a","a","b"]
#   ]

class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        if len(s) == 0:
            return []
        result = []
        #get all separate occasion
        current = [[s[0]]]
        for i in range(1,len(s)):
            new = []
            new_char = s[i]
            for j in current:
                first_case = j[:]
                first_case.append(new_char)
                new.append(first_case)

                second_case = j[:]
                new_last = second_case[len(second_case) - 1] + new_char
                if self.is_palindrome(new_last):
                    second_case[-1] = new_last
                    new.append(second_case)
                elif len(second_case) > 1 and second_case[-2] == new_char:
                    second_case[-2] = new_char + new_last
                    second_case.pop(-1)
                    new.append(second_case)
            current = new
        #remove those are not palindrome
        for i in current:
            is_ok = True
            for j in i:
                if not self.is_palindrome(j):
                    is_ok = False
                    break
            if is_ok:
                result.append(i)
        return result

    def is_palindrome(self, word):
        for i in range(len(word)/2):
            if word[i] != word[-(i+1)]:
                return False
        return True
