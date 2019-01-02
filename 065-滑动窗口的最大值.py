# -*- coding:utf-8 -*-
'''
利用python自带的堆来实现
python堆heapq为最小堆，用最大堆时，把元素取反即可
没有peak/top操作，所以在pop之后，要重新push，另外每次remove之后都需要重新堆序化，保证窗口一直是堆

'''
import heapq
class Solution:
    def maxInWindows(self, num, size):
        if size == 0 or size > len(num):return []
        myheap = [-num[i] for i in range(size)]
        heapq.heapify(myheap)
        res = []
        for i in range(size, len(num)+1):
            t = heapq.heappop(myheap)
            res.append(-t)
            heapq.heappush(myheap, t)
            myheap.remove(-num[i-size])
            #这里不是pop删除，所以删除后不一定保持堆序，需要重新变成堆序
            heapq.heapify(myheap)
            if i < len(num):heapq.heappush(myheap, -num[i])
        return res 

sol = Solution()
print sol.maxInWindows([2,3,4,2,6,2,5,1],3)