# Author  :  Yagao0o
# Date    :  2015-02-
# Source  :  https://oj.leetcode.com/problems/unique-binary-search-trees-ii/

# Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.
#
# For example,
# Given n = 3, your program should return all 5 unique BST's shown below.
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        if n == 0:
            return [None]
        trees_list = []
        for input_string in self.get_input_strings(n):
            trees_list.append(self.build_tree(input_string))
        return trees_list

    def get_input_strings(self, n):
        result_dic = {0: [], 1: [[1]]}
        for i in range(2, n + 1):
            #build i numbers
            result_i = []
            for root_number in range(1, i + 1):
                left_numbers = range(1, root_number)
                right_numbers = range(root_number + 1, i + 1)
                if not left_numbers:
                    for right_situation in result_dic[len(right_numbers)]:
                        new_result = [root_number]
                        for k in right_situation:
                            new_result.append(right_numbers[k - 1])
                        result_i.append(new_result)
                elif not right_numbers:
                    for left_situation in result_dic[len(left_numbers)]:
                        new_result = [root_number]
                        for k in left_situation:
                            new_result.append(left_numbers[k - 1])
                        result_i.append(new_result)
                else:
                    for left_situation in result_dic[len(left_numbers)]:
                        for right_situation in result_dic[len(right_numbers)]:
                            new_result = [root_number]
                            for k in left_situation:
                                new_result.append(left_numbers[k - 1])
                            for k in right_situation:
                                new_result.append(right_numbers[k - 1])
                            result_i.append(new_result)
                result_dic[i] = result_i
        return result_dic[n]

    def build_tree(self, input_list):
        root = None
        if input_list:
            root = TreeNode(input_list.pop(0))
        for number in input_list:
            current = root
            while current:
                if number < current.val:
                    if current.left:
                        current = current.left
                    else:
                        current.left = TreeNode(number)
                        current = None
                else:
                    if current.right:
                        current = current.right
                    else:
                        current.right = TreeNode(number)
                        current = None
        return root

# TODO reconsider the algo
# passed the oj, but good enough......
