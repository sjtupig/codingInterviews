# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while n != 0:
            count += 1
            n = n & (n-1)
        return count
        #如果n大于0，直接计算即可，如果n小于0，计算2的32次方加上n的结果中1的个数。
        #return bin(n).replace("0b","").count("1") if n>=0 else bin(2**32+n).replace("0b","").count("1")
        