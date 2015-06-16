# Author  :  Yagao0o
# Date    :  2015-02-19
# Source  :  https://leetcode.com/problems/implement-trie-prefix-tree/

# Implement a trie with insert, search, and startsWith methods.
#
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.


class TrieNode:
    # Initialize your data structure here.
    def __init__(self, c = ''):
        self.val = c
        self.children = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
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

    #
    # def ins(self, node, word):
    #     if word == '':
    #         node.children.append(TrieNode())
    #         return
    #     for child_node in node.children:
    #         if child_node.val == word[0]:
    #             self.ins(child_node, word[1:])
    #             return
    #     new_node = word[0]
    #     self.ins(new_node, word[1:])
    #     node.children.append(new_node)

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
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
                return False
        for child in current_node.children:
            if child.val == '':
                return True
        return False

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        current_node = self.root
        word = prefix
        while len(word) > 0:
            is_find = False
            for child in current_node.children:
                if child.val == word[0]:
                    current_node = child
                    word = word[1:]
                    is_find = True
                    break
            if not is_find:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
