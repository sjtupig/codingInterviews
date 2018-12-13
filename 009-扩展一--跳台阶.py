# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 1:
            return 1
        if number == 2:
            return 2
        res = [0]*(number+1)
        res[1] = 1
        res[2] = 2
        for i in range(3,number+1):
            res[i]= res[i-1] + res[i-2]
        
        return res[number]