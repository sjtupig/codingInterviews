# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        left = [reduce(lambda x,y:x*y,A[:i],1) for i in range(len(A))]
        right = [reduce(lambda x,y:x*y,A[i+1:],1) for i in range(len(A))]
        
        return [left[i]*right[i] for i in range(len(A))]