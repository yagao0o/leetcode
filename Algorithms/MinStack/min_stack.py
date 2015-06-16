# Author  :  Yagao0o
# Date    :  2014-11-10
# Source  :  https://oj.leetcode.com/problems/min-stack/

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.

class MinStack:
    def __init__(self):
        self.numbers = []
        self.min = 0
        self.len = 0

    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.len += 1
        if not self.numbers:
            self.min = x
        elif x < self.min:
            self.min = x
        self.numbers.append(x)

    # @return nothing
    def pop(self):
        if self.numbers:
            self.len -= 1
            if self.numbers.pop() == self.min:
                self.count_min()

    # @return an integer
    def top(self):
        if self.numbers:
            return self.numbers[self.len - 1]
        else:
            return 0

    # @return an integer
    def getMin(self):
        return self.min

    def count_min(self):
        if self.numbers:
            self.min = min(self.numbers)
        else:
            self.min = 0