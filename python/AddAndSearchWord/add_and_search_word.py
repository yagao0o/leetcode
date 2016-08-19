# Author  :  Yagao0o
# Date    :  2015/6/16
# Source  :  https://leetcode.com/problems/add-and-search-word-data-structure-design/

# Design a data structure that supports the following two operations:
#
# void addWord(word)
# bool search(word)
# search(word) can search a literal word or a regular expression string containing only letters a-z or '.' .
# A '.' means it can represent any one letter.
#
# For example:
#
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# Note:
# You may assume that all words are consist of lowercase letters a-z.


class TrieNode:
    # Initialize your data structure here.
    def __init__(self, c = ''):
        self.val = c
        self.children = []


class WordDictionary:
    # initialize your data structure here.
    def __init__(self):
        self.root = TrieNode()
        self.cache = {}

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        self.cache = {}
        current_node = self.root
        while len(word) > 0:
            is_find = False
            for child in current_node.children:
                if child.val == word[0]:
                    current_node = child
                    word = word[1:]
                    is_find = True
                    break
            if not is_find:
                new_node = TrieNode(word[0])
                word = word[1:]
                current_node.children.append(new_node)
                current_node = new_node
        current_node.children.append(TrieNode())

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        word_bak = word
        if word in self.cache:
            return self.cache[word]
        current_list = [self.root]
        while len(word) > 0 and current_list:
            next_level = []
            if word[0] == '.':
                for node in current_list:
                    for child in node.children:
                        next_level.append(child)
            else:
                for node in current_list:
                    for child in node.children:
                        if child.val == word[0]:
                            next_level.append(child)
            current_list = next_level
            word = word[1:]
        for node in current_list:
            for child in node.children:
                if child.val == '':
                    self.cache[word_bak] = True
                    return True
        self.cache[word_bak] = False
        return False
