# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        #二叉树系列化 + kmp算法
        def get_tree_str(root):
            if not root:
                return '' 
            res = ''
            res += str(root.val)
            res += get_tree_str(root.left)
            res += get_tree_str(root.right)
            return res
        
        strpRoot1 = get_tree_str(pRoot1)
        strpRoot2 = get_tree_str(pRoot2)
        print strpRoot1
        print strpRoot2
        return strpRoot2 in strpRoot1 if strpRoot2 else False