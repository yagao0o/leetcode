# Author  :  Yagao0o
# Date    :  2015-05-23
# Source  :  https://leetcode.com/problems/word-ladder/

# Given two words (beginWord and endWord),
# nd a dictionary, find the length of shortest transformation sequence from beginWord to endWord, such that:
#
# Only one letter can be changed at a time
# Each intermediate word must exist in the dictionary
# For example,
#
# Given:
# start = "hit"
# end = "cog"
# dict = ["hot","dot","dog","lot","log"]
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
#
# Note:
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.

class Solution:
    # @param beginWord, a string
    # @param endWord, a string
    # @param wordDict, a set<string>
    # @return an integer
    def ladderLength(self, beginWord, endWord, wordDict):
        if beginWord == endWord:
            return  1
        if self.is_neighbour(beginWord, endWord):
            return 2
        left_set = set([beginWord])
        right_set = set([endWord])
        left_depth = 1
        right_depth = 1
        left_remain = wordDict.copy()
        right_remain = wordDict.copy()
        while left_set and right_set:
            new_set = set([])
            if len(left_remain) * len(left_set) < len(right_remain) * len(right_set):
                while left_set:
                    current_word = left_set.pop()
                    if self.is_neighbour(current_word, endWord):
                        return left_depth + 1
                    for new_word in self.create_word_neighbour_set(current_word):
                        if new_word in left_remain:
                            left_remain.remove(new_word)
                            new_set.add(new_word)
                left_depth += 1
                left_set = new_set
            else:
                while right_set:
                    current_word = right_set.pop()
                    if self.is_neighbour(current_word, beginWord):
                        return  right_depth + 1
                    for new_word in self.create_word_neighbour_set(current_word):
                        if new_word in right_remain:
                            right_remain.remove(new_word)
                            new_set.add(new_word)
                right_set = new_set
                right_depth += 1
            if left_set & right_set:
                return left_depth + right_depth - 1
        return 0


    def create_word_neighbour_set(self, word):
        result_set = set([])
        for i in range(len(word)):
            for j in range(26):
                result_set.add(word[:i] + chr(ord('a') + j) + word[i + 1:])
        return result_set

    def is_neighbour(self, word1, word2):
        differs = 0
        for i in range(len(word1)):
            if  word1[i] != word2[i]:
                differs += 1
                if differs > 1:
                    return False
        return True