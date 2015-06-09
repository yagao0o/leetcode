# Author  :  Yagao0o
# Date    :  2015-06-09
# Source  :  https://leetcode.com/problems/binary-search-tree-iterator/

# Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
#
# Calling next() will return the next smallest number in the BST.
#
# Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
#
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:
    node_list = []
    # @param root, a binary search tree's root node
    def __init__(self, root):
        current = root
        while current:
            self.node_list.insert(0, current)
            current = current.left

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self.node_list) > 0

    # @return an integer, the next smallest number
    def next(self):
        current_node = self.node_list.pop(0)
        self.__init__(current_node.right)
        return current_node.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())