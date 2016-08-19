# Author  :  Yagao0o
# Date    :  2015-03-01
# Source  :  https://oj.leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

# Follow up for problem "Populating Next Right Pointers in Each Node".
#
# What if the given tree could be any binary tree? Would your previous solution still work?
#
# Note:
#
# You may only use constant extra space.
# For example,
# Given the following binary tree,
#          1
#        /  \
#       2    3
#      / \    \
#     4   5    7
# After calling your function, the tree should look like:
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \    \
#     4-> 5 -> 7 -> NULL

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        current = [root]
        while current:
            new = []
            for i in range(len(current) - 1):
                if current[i]:
                    current[i].next = current[i + 1]
                    if current[i].left:
                        new.append(current[i].left)
                    if current[i].right:
                        new.append(current[i].right)
            last = current[len(current) - 1]
            last.next = None
            if last.left:
                new.append(last.left)
            if last.right:
                new.append(last.right)
            current = new