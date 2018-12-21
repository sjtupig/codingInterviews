#暴力解法：超时
# -*- coding:utf-8 -*-
class Solution1:
    def GetUglyNumber_Solution(self, index):
        # write code here
        #ugly = 5**a * 3**b * 2**c, 看a,b,c取值，0-无穷
        def is_ugly(a, mul):
            for i in mul[::-1]:
                while a%i==0:
                    a=a/i
                if a==1:return True
            return False
        cnt = 0
        i = 1
        mul = [2,3,5]
        while True:
            if is_ugly(i, mul):
                cnt += 1
                mul.append(i)
            if cnt == index-1:
                return i 
            i += 1

# -*- coding:utf-8 -*-
###重点是每次都只加进来一个数字
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        #ugly = 5**a * 3**b * 2**c, 看a,b,c取值，0-无穷
        res = [1,]
        nums = 1
        while nums < index:
            max_num = max(res)
            candidate = []
            for i in res:
                if 2*i>max_num:
                    candidate.append(2*i) 
                    break 
            for i in res:
                if 3*i>max_num:
                    candidate.append(3*i)  
                    break
            for i in res:
                if 5*i>max_num:
                    candidate.append(5*i)  
                    break
            res.append(min(candidate))
            nums+=1
        return res[index-1] if index > 0 else 0

#更快解法，每次都记录乘数，因为上一次2*res[low_2]才大于max_num，所以这轮计算式，low_2之前的数都不可能比max_num大，从此往后计算，更快
# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        #ugly = 5**a * 3**b * 2**c, 看a,b,c取值，0-无穷
        res = [1,]
        nums = 1
        low_2,low_3,low_5 = 0,0,0
        while nums < index:
            max_num = max(res)
            candidate = []
            for i in range(low_2,len(res)):
                if 2*res[i]>max_num:
                    candidate.append(2*res[i]) 
                    low_2 = i 
                    break 
            for i in range(low_3,len(res)):
                if 3*res[i]>max_num:
                    candidate.append(3*res[i])
                    low_3 = i 
                    break
            for i in range(low_5,len(res)):
                if 5*res[i]>max_num:
                    candidate.append(5*res[i]) 
                    low_5 = i 
                    break
            res.append(min(candidate))
            nums+=1
        return res[index-1] if index > 0 else 0
sol = Solution2()
print(sol.GetUglyNumber_Solution(1))
print(sol.GetUglyNumber_Solution(2))
print(sol.GetUglyNumber_Solution(3))
print(sol.GetUglyNumber_Solution(4))
print(sol.GetUglyNumber_Solution(5))