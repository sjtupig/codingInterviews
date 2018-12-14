# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        #res = pHead
        #pHead = pHead.next
        res = None
        while pHead:
            q = pHead
            pHead = pHead.next
            q.next = res
            res = q
        return res 