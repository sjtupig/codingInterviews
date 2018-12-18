# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root: #若为空返回空列表
            return []
        res = []#返回值
        deque = [] #队列保存结点
        deque.append(root)
        while deque:
            t = deque[0]
            del deque[0] #出队
            if t.left:
                deque.append(t.left)#入队
            if t.right:
                deque.append(t.right)#入队
            res.append(t.val)
        return res
