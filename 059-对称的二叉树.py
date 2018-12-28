# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
朴素解题思路：先得到二叉树的镜像，再比较
'''
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        #得到镜像
        if not pRoot: return True
        def getMirror(pRoot, newRoot):
            #newRoot = TreeNode(pRoot.val)
            if not pRoot or not newRoot:return
            #print('pRoot:',pRoot.val)
            #print('newRoot:',newRoot.val)
            newRoot.left = TreeNode(pRoot.right.val) if pRoot.right else None
            newRoot.right = TreeNode(pRoot.left.val) if pRoot.left else None
            getMirror(pRoot.right, newRoot.left)
            getMirror(pRoot.left, newRoot.right)
            return newRoot
        #比较
        def compare(pRoot, newRoot):
            if not pRoot and not newRoot:return True
            if pRoot and not newRoot:return False
            if not pRoot and newRoot:return False
            return pRoot.val==newRoot.val and compare(pRoot.left, newRoot.left) and compare(pRoot.right, newRoot.right)
        
        newRoot = TreeNode(pRoot.val)
        newRoot = getMirror(pRoot, newRoot)
        return compare(pRoot, newRoot)


#上述朴素办法可以合并起来，即获取镜像的时候比较
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        #得到镜像
        if not pRoot: return True
        def compare(left, right):
            if left and right:
                return left.val==right.val and compare(left.left, right.right) and compare(left.right, right.left)
            elif not left and not right:
                return True
            elif not left and right:
                return False
            elif left and not right:
                return False 
        
        return compare(pRoot.left, pRoot.right)