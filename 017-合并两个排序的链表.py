# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        res = None
        while pHead1 or pHead2:
            if pHead1 and pHead2:
                if pHead1.val <= pHead2.val:
                    node = ListNode(pHead1.val)
                    node.next = res
                    res = node
                    pHead1 = pHead1.next
                else:
                    node = ListNode(pHead2.val)
                    node.next = res
                    res = node
                    pHead2 = pHead2.next
            elif pHead1 and not pHead2:
                node = ListNode(pHead1.val)
                node.next = res
                res = node
                pHead1 = pHead1.next
            elif not pHead1 and pHead2:
                node = ListNode(pHead2.val)
                node.next = res
                res = node
                pHead2 = pHead2.next
        #因为链表是头插入，所以这里要对链表进行翻转（这样会比尾插入更快）
        resn = None
        while res:
            node = ListNode(res.val)
            node.next = resn
            resn = node
            res = res.next
        return resn 
        #以为递归写法
        '''
        def merge(pHead1, pHead2):
            if pHead1 == None:
                return pHead2
            if pHead2 == None:
                return pHead1
            if pHead1.val <= pHead2.val:
                pHead1.next = merge(pHead1.next, pHead2)
                return pHead1
            else:
                pHead2.next = merge(pHead1, pHead2.next)
                return pHead2
        return merge(pHead1, pHead2)
        '''