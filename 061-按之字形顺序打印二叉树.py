# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:return []
        nowline = [pRoot]
        nextline = []
        if pRoot.left:nextline.append(pRoot.left)
        if pRoot.right:nextline.append(pRoot.right)
        res = []
        left_to_right = 1
        while nowline:
            if left_to_right:
                res.append([i.val for i in nowline])
                left_to_right = 1-left_to_right
            else:
                res.append([i.val for i in nowline[::-1]])
                left_to_right = 1-left_to_right
            t = []
            for i in nextline:
                if i.left:t.append(i.left)
                if i.right:t.append(i.right)
            nowline = nextline
            nextline = t
        return res 