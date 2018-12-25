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
                if not res:
                    res=[array[l],array[r]]
                else:
                    if array[l]*array[r] < res[0]*res[1]:
                        res=[array[l],array[r]]
                l+=1
                r-=1
        return res


sol = Solution()
print(sol.FindNumbersWithSum([], 8))