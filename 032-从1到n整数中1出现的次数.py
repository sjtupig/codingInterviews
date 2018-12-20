# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        return sum([i.count('1') for i in [str(t) for t in range(1,n+1)]])