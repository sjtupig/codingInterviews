# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        '''
        需要考虑一些边界情况：  '        +1', '+', '        ', '++3', '123-2'

        '''
        if s.strip() == '':return 0
        if len(s.strip()) == 1 and s.strip()[0] in ('+','-'):return 0  # ++123会在下面剔除
        s_list = list(s.strip())
        for i, val in enumerate(s_list):
            if i ==0 :
                if val not in ['+','-','1','2','3','4','5','6','7','8','9','0']:
                    return 0
            else:
                if val not in ['1','2','3','4','5','6','7','8','9','0']:
                    return 0 
        tag = 1
        if s_list[0] == '-':
            tag = -1
            s_list.remove(s_list[0])
        elif s_list[0] == '+':
            tag = 1
            s_list.remove(s_list[0])
        nums = [int(i) for i in s_list]
        res = 0
        for i in nums:
            res = 10 * res + i 
        
        return tag*res


sol = Solution()
print(sol.StrToInt('+2147483647'))
print(sol.StrToInt('    1a33'))
print(sol.StrToInt('      '))
print(sol.StrToInt('    +  '))
