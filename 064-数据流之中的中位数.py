# -*- coding:utf-8 -*-
from __future__ import division
class Solution:
    def __init__(self):
        self.stream = []
    def Insert(self, num):
        # write code here
        self.stream.append(num)
    def GetMedian(self,N):
        # write code here
        t = sorted(self.stream)
        length = len(t)
        if length%2:
            return t[int(length/2)]
        else:
            return (t[int(length/2)]+t[int(length/2)-1])/2.0

#在线算法， 堆实现，效果更好