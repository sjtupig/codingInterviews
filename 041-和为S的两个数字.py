# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        l, r = 0, len(array)-1
        res = []
        while l < r:
            if array[l]+array[r] < tsum:
                l+=1
            if array[l]+array[r] > tsum:
                r-=1
            if array[l]+array[r] == tsum:
                #找到第一队可以直接返回，因为这个乘积一定最小，1*6<2*3
                '''
                if not res:
                    res=[array[l],array[r]]
                else:
                    if array[l]*array[r] < res[0]*res[1]:
                        res=[array[l],array[r]]
                l+=1
                r-=1'''
                return [array[l],array[r]]
        return res


sol = Solution()
print(sol.FindNumbersWithSum([], 8))
