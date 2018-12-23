# -*- coding:utf-8 -*-
#以下解法默认链表无环
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:return 
        len1,len2 = 0,0 
        t = pHead1
        while t:
            len1 += 1
            t = t.next
        t = pHead2
        while t:
            len2 += 1
            t = t.next
        t_short,len_short = (pHead1,len1) if len1 < len2 else (pHead2,len2)
        t_long,len_long = (pHead2,len2) if len1 < len2 else (pHead1,len1)
        first_steps = len_long-len_short
        while first_steps:
            t_long = t_long.next
            first_steps -= 1
        while t_long:
            if t_long == t_short:
                return t_long
            else:
                t_long = t_long.next
                t_short = t_short.next
        return 
        

a = ListNode(10)
b = ListNode(11)
c = ListNode(5)
pHead1 = ListNode(1)
pHead2 = ListNode(2)
pHead1.next=a
a.next=b 
pHead2.next=c 
c.next=a 

sol=Solution()
print(sol.FindFirstCommonNode(pHead1,pHead2).val)