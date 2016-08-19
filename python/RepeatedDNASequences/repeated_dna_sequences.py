# Author  :  Yagao0o
# Date    :  2015/6/24
# Source  :  https://leetcode.com/problems/repeated-dna-sequences/

# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T,
# for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
#
# Write a function to find all the 10-letter-long sequences
# substrings) that occur more than once in a DNA molecule.
#
# For example,
#
# Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
#
# Return:
# ["AAAAACCCCC", "CCCCCAAAAA"].


class Solution:
    # @param {string} s
    # @return {string[]}
    def findRepeatedDnaSequences(self, s):
        dic = {}
        for i in xrange(len(s) - 9):
            dic[s[i:i+10]] = dic.get(s[i:i+10],0) + 1
        return [res for res in dic.keys() if dic[res] > 1]

#I consider it more complex, I used a trie. But not efficient as it.