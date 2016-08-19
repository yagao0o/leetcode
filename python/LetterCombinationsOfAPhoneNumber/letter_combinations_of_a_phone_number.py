# Author  :  Yagao0o
# Date    :  2015-02-03
# Source  :  https://oj.leetcode.com/problems/letter-combinations-of-a-phone-number/

# Given a digit string, return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below.
#
# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:
# Although the above answer is in lexicographical order, your answer could be in any order you want.

class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        letter_dic = {"0": [" "], "1": [""], "2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"],
                      "5": ["j", "k","l"], "6": ["m", "n","o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"],
                      "9": ["w", "x", "y", "z"]}
        result = [""]
        for dig in digits:
            current = []
            if dig == "1":
                continue
            for letter in letter_dic[dig]:
                for combination in result:
                    current.append(combination + letter)
            result = current
        return result

