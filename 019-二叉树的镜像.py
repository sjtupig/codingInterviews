# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        
        def rev(root):
            if not root:
                return None
            root.left, root.right = root.right, root.left
            rev(root.left)
            rev(root.right)
            return root
        
        return rev(root)