# -*- coding:utf-8 -*-
#循环链表解法
class LinkNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n == 0 or m == 0:return -1
        head = LinkNode(0)
        tail = head
        for i in range(1,n):
            tail.next = LinkNode(i)
            tail = tail.next
        tail.next = head
        while head.next != head:
            if m == 1:  #每次把头链表干掉，注意要更新尾指针的next
                head = head.next
                tail.next = head
            else:
                t = m-2
                while t:
                    head = head.next
                    t -= 1
                head.next = head.next.next 
                head = head.next 
            '''print '*************************'
            t = head
            while t.next !=head:
                print t.val
                t = t.next
            print t.val
            print '*************************'''
        return head.val

sol = Solution()
print sol.LastRemaining_Solution(5,2)

#或者用list模拟循环链表，用模运算来模拟（当迭代到list结尾时，要从头开始）

#递推公式解法

class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if not n or not m: return -1
        childs = list(range(n))
        i = 0
        while len(childs) > 1:
            index = (i %len(childs)+ (m-1)%len(childs))%len(childs)
            childs.remove(childs[index])
            i = index 
        return childs[0]

sol = Solution()
print sol.LastRemaining_Solution(5,2)