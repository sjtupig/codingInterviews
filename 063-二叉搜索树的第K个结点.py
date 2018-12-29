
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        #二叉搜索树的中序遍历正好是一个递增的序列, 因此中序遍历的第K个结点就是二叉搜索树的第K个节点
        if k == 0:return 
        def get(pRoot):
            if not pRoot:return 
            get(pRoot.left)
            self.a.append(pRoot)
            get(pRoot.right)

        self.a = []
        get(pRoot)
        return self.a[k-1] if k <= len(self.a) else None


#非递归实现
