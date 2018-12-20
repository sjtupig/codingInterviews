# -*- coding:utf-8 -*-
class Solution1:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        tinput.sort()
        return tinput[:k] if k <= len(tinput) else []


# -*- coding:utf-8 -*- 
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k > len(tinput) or k ==0:return []
        #if k == len(tinput):return tinput
        res = tinput[:k]
        for i in range(k,len(tinput)):
            if tinput[i] < max(res):
                res[res.index(max(res))] = tinput[i] #这里不能remove,在append,因为remove会改变list
            #print(res)
        res.sort()
        return res

#更多办法请见：https://github.com/gatieme/CodingInterviews/tree/master/030-%E6%9C%80%E5%B0%8F%E7%9A%84K%E4%B8%AA%E6%95%B0

tinput = [4,5,1,6,2,7,3,8]
sol = Solution2()
print(sol.GetLeastNumbers_Solution(tinput, 8))