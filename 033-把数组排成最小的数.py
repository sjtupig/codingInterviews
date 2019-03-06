# -*- coding:utf-8 -*-
from functools import cmp_to_key
class Solution:
    
    def PrintMinNumber(self, numbers):
        # write code here
        def cp(x,y):
            if int(x+y) < int(y+x):
                return -1
            elif int(x+y) > int(y+x):
                return 1
            else:
                return 0
        if not numbers:return ''
        res = sorted(list(map(str,numbers)), key = cmp_to_key(cp))

        return int(''.join(res))


sol = Solution()
print(sol.PrintMinNumber([3,32,321]))