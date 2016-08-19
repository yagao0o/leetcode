# Author  :  Yagao0o
# Date    :  2015-06-02
# Source  :  https://leetcode.com/problems/single-number-ii/

# Given a string s and a dictionary of words dict,
# determine if s can be segmented into a space-separated sequence of one or more dictionary words.
# For example, given
# s = "leetcode",
# dict = ["leet", "code"].
# Return true because "leetcode" can be segmented as "leet code".


class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        check = [False] * (len(s) + 1)
        check[0] = True
        for i in range(len(s)):
            for word in wordDict:
                if i - len(word) + 1 >= 0 and check[i - len(word) + 1] and s[i - len(word) + 1:i + 1] == word:
                    check[i + 1] = True
                    break
        return check[-1]

    def wordBreak_bad_version(self, s, wordDict):
        # earlier version code by yagao0o
        # not an efficient one
        # but i still think the way is good.
        current_length = 0
        length_stack = []
        new_length = 1
        max_length = 0
        for word in wordDict:
            max_length = max(max_length, len(word))
        while True:
            if current_length == len(s):
                return True
            if s[current_length:current_length + new_length] in wordDict:
                length_stack.insert(0, new_length)
                current_length += new_length
                new_length = 1
            else:
                new_length += 1
                if new_length + current_length > len(s) or new_length > max_length:
                    if not length_stack:
                        return False
                    new_length = length_stack.pop(0)
                    current_length -= new_length
                    new_length += 1
        return False