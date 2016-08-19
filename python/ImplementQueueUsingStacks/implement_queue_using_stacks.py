# Author  :  Yagao0o
# Date    :  2015/8/6
# Source  :  https://leetcode.com/problems/implement-queue-using-stacks/

# Implement the following operations of a queue using stacks.
#
# push(x) -- Push element x to the back of queue.
# pop() -- Removes the element from in front of queue.
# peek() -- Get the front element.
# empty() -- Return whether the queue is empty.
# Notes:
# You must use only standard operations of a stack -- which means only push to top,
#    peek/pop from top, size, and is empty operations are valid.
# Depending on your language, stack may not be supported natively.
#    You may simulate a stack by using a list or deque
#    (double-ended queue), as long as you use only standard operations of a stack.
# You may assume that all operations are valid (for example,
# no pop or peek operations will be called on an empty queue).

class Stack:
    def __init__(self):
        self.count = 0
        self.max_length = 0
        self.item_list = []

    def push_to_top(self, n):
        if self.count == self.max_length:
            self.item_list.append(n)
            self.max_length += 1
        else:
            self.item_list[self.count] = n
        self.count += 1
    def peek_from_top(self):
        return self.item_list[self.count - 1]

    def pop_from_top(self):
        self.count -= 1
        return self.item_list[self.count]

    def size(self):
        return self.count

    def is_empty(self):
        return self.count == 0

class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.main_stack = Stack()

    # @param x, an integer
    # @return nothing
    def push(self, x):
        temp_stack = Stack()
        while not self.main_stack.is_empty():
            temp_stack.push_to_top(self.main_stack.pop_from_top())
        self.main_stack.push_to_top(x)
        while not temp_stack.is_empty():
            self.main_stack.push_to_top(temp_stack.pop_from_top())

    # @return nothing
    def pop(self):
        return self.main_stack.pop_from_top()


    # @return an integer
    def peek(self):
        return self.main_stack.peek_from_top()

    # @return an boolean
    def empty(self):
        return self.main_stack.is_empty()
