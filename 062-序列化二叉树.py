# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Serialize(self, root):
        # write code here
        s = ''
        if not root: 
            return  '#!'
        return s + str(root.val) + '!' + self.Serialize(root.left) + self.Serialize(root.right)
        
    def Deserialize(self, s):
        # write code here
        def get_string(l):
            if l[0] == '#':
                l.remove(l[0])
                return None
            root = TreeNode(int(l[0]))
            #注意，修改传入的参数这步很重要
            l.remove(l[0])
            root.left = get_string(l)
            root.right = get_string(l)
            return root 
        l = s.split('!')
        return get_string(l)