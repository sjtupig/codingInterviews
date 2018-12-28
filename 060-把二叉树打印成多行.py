# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:return []
        res = []
        now = [pRoot] if pRoot else []
        nexts = []
        #这里默认了pRoot不为空，所以在一开始判断若pRoot为空，直接返回
        if pRoot.left: nexts.append(pRoot.left) 
        if pRoot.right: nexts.append(pRoot.right) 
        while now:
            res.append([i.val for i in now])
            tp = []
            for i in nexts:
                if i.left: tp.append(i.left) 
                if i.right: tp.append(i.right) 
            now = nexts
            nexts = tp 
        return res 

#用两个节点，
#last表示正在打印的当前行的最右节点
#nlast表示下一行的最右节点，，而这各恰恰是每次新加入的节点