'''
################################################################################################################################

                                       虚拟头结点

###############################################################################################################################

'''
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#直接在原链表上做
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        
        #空或者只有一个节点，直接返回
        if not pHead or not pHead.next:return pHead
        #先看排除头的重复
        while pHead and pHead.next and pHead.val == pHead.next.val: #这一步是判断，头部是否有重复，如果有重复，那就到下面去去重（因为可能由111222333345这种情况，所以要这么写）
            flag = 0
            while pHead and pHead.next and pHead.val == pHead.next.val:
                flag = 1
                pHead = pHead.next
            if flag: pHead = pHead.next
        #节点1 != 节点2
        t = pHead
        while t and t.next and t.next.next:
            if t.next.val == t.next.next.val:
                t.next = t.next.next.next
                continue 
            t = t.next
        return pHead
#新建一个链表头来做

 #-*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        
        #空或者只有一个节点，直接返回
        #设置一个trick, 作为头指针, 这样我们无需单独考虑第一个元素
        newHead = ListNode('trick')
        tail = newHead
        while pHead:
            if pHead.next:
                if pHead.val != pHead.next.val:
                    tail.next = pHead
                    tail = tail.next
                    pHead = pHead.next
                else:
                    while pHead and pHead.next and pHead.val == pHead.next.val:
                        pHead = pHead.next
                    pHead = pHead.next
                    print pHead.val if pHead else None 
                    #这里是为了应对如果结尾重复了
                    if not pHead:
                        tail.next = None 
            else:
                tail.next = pHead
                print 'add:', pHead.val 
                tail = tail.next
                pHead = pHead.next

        return newHead.next

a = ListNode(1)
b = ListNode(1)
c = ListNode(2)
d = ListNode(3)
e = ListNode(3)
f = ListNode(4)
g = ListNode(5)
h = ListNode(5)
a.next = b; b.next=c; c.next=d; d.next=e;e.next=f;f.next=g;g.next=h 
sol = Solution()
print sol.deleteDuplication(a).next.next.val



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead == None or pHead.next == None:
            return pHead
        new_head = ListNode(-1)
        new_head.next = pHead
        pre = new_head
        p = pHead
        nex = None
        while p != None and p.next != None:
            nex = p.next
            if p.val == nex.val:
                while nex != None and nex.val == p.val:
                    nex = nex.next
                pre.next = nex
                p = nex
            else:
                pre = p
                p = p.next
        return new_head.next

'''
先不管三七二十一把所有节点的值放到一个列表中，再筛选出值数量为1的值。'''

class Solution:
    def deleteDuplication(self, pHead):
        res = []
        while pHead:
            res.append(pHead.val)
            pHead = pHead.next
        res = list(filter(lambda c: res.count(c) == 1, res))
        dummy = ListNode(0)
        pre = dummy
        for i in res:
            node = ListNode(i)
            pre.next = node
            pre = pre.next
        return dummy.next