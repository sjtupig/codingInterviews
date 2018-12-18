# -*- coding:utf-8 -*-
from functools import reduce
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        def if_fyseq(a):
            if len(a) <= 1:
                return True
            root = a[-1]
            del a[-1]
            l = -1
            for i in a:
                if i < root:
                    l += 1 #a[l+1]>root, l是最后一个<root的下标
            #判断右边是否都大于root
            if l+1 <= len(a) - 1 and (not reduce(lambda x,y:x&y, map(lambda x:x > root, a[l+1:]))):
                return False
            
            return if_fyseq(a[:l+1]) & (if_fyseq(a[l+1:]) if l+1<=len(a)-1 else if_fyseq([]))

        #return 'Yes' if if_fyseq(sequence) else 'No'
        if sequence == []:
            return False
        return if_fyseq(sequence)

so = Solution()
#sequence1 = [2,9,8,17,15]
sequence2 = [7,4,6,5]

#print(so.VerifySquenceOfBST(sequence1))
print(so.VerifySquenceOfBST(sequence2))