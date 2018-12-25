# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        res = []
        now = []
        l, r = 1,1#连续正数，从1开始 
        #2*(int(tsum/2)+1) > tsum
        #这里终止条件不用tsum，可以提速
        while r <= int(tsum/2)+2:#至少要有两个数，所以[tsum]不符合条件, 100 = 50+51这种情况 ，这里用+2是因为，对于tsum=9，仅+1,不会去计算4,5可以模拟运行一下
            if sum(now) < tsum:
                now.append(r)
                r += 1
            if sum(now) == tsum:
                if len(now)>1:
                    res.append(now[:])  #这里大坑，如果res.append(now)，那么添加的是row的引用，now变的话，res里的结果也会变，这里必须用now[:]
                now.append(r)
                r += 1 
            if sum(now) > tsum:
                now.remove(l)
                l += 1
        return res  


# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        res = []
        now = []
        l, r = 1,1#连续正数，从1开始 
        #2*(int(tsum/2)+1) > tsum
        #这里终止条件不用tsum，可以提速
        epos = 1 
        while r < tsum:#至少要有两个数，所以[tsum]不符合条件, 100 = 50+51这种情况
            epos+=1 
            while sum(now) < tsum:
                now.append(r)
                r += 1
            if sum(now) == tsum:
                if len(now)>1:
                    res.append(now[:])  #这里大坑，如果res.append(now)，那么添加的是row的引用，now变的话，res里的结果也会变，这里必须用now[:]
                now.append(r)
                r += 1 
            while sum(now) > tsum:
                now.remove(l)
                l += 1
        return res 

sol = Solution()
print(sol.FindContinuousSequence(9))