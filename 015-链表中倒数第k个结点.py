# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        #坑！！！！！！！！！！！！！！！！！！！返回node
        #python list索引是o(1)很快
        res = []
        while head:
            res.append(head)
            head = head.next
        if 1 <= k <= len(res):
            return res[-k]
        return 

        #注意这题也可以用双指针走,双指针法 其实就是第一个指针right先向前走K步，然后left和right一起走，此时两个指针差别K步，那么当right走到链表尾部的时候，left指向的就是倒数第K个节点

            #期间要注意的问题有

            #链表可能为NULL

            #链表长度可能没有K个