# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        # write code here
        self.stack1.append(node)
    def pop(self):
        # return xx
        if len(self.stack2) > 0:
            return self.stack2.pop()
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        if len(self.stack2) > 0:
            return self.stack2.pop()
            