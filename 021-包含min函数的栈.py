# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = [] #栈顶保存栈中当前的最小值
    def push(self, node):
        # write code here
        self.stack1.append(node)
        if (self.stack2 and node <= self.stack2[-1]) or not self.stack2:
            self.stack2.append(node)
    def pop(self):
        # write code here
        #如果出栈的元素和保存最小值的栈顶值一样，则保存最小值的栈顶出栈
        if self.stack1:
            t = self.stack1.pop()
            if t == self.stack2[-1]:
                t = self.stack2.pop()
            return t
    def top(self):
        # write code here
        if self.stack1:
            return self.stack1[-1]
    def min(self):
        # write code here
        if self.stack2:
            return self.stack2[-1]