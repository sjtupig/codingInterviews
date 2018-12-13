# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        #两个要点：1、前序的第一个永远是根节点
        #		  2、前序中左子树个数 = 中序中左子树个数
        def get_tree(root, pre, tin):
            #不用这一段是因为，列表长度可能由2直接变为0，某一个子树为0，这样会报错（只写len==1而不写len==0）
            '''if len(pre) == 1:
                root.val = pre[0]
                root.left = None
                root.right = None
                return root'''
            if len(pre) == 0:
                return None
            root.val = pre[0]
            root_index = tin.index(pre[0])
            root.left = get_tree(TreeNode(None), pre[1:root_index+1], tin[:root_index])
            root.right = get_tree(TreeNode(None), pre[root_index+1:], tin[root_index+1:])
            
            return root
        return get_tree(TreeNode(None) , pre, tin)