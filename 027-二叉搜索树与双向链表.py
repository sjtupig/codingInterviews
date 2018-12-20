# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution1:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return 
        self.nodes = []
        self.getmidseq(pRootOfTree)
        for i in range(len(self.nodes)-1):
            self.nodes[i].right = self.nodes[i+1]
        for i in range(1, len(self.nodes)):
            self.nodes[i].left = self.nodes[i-1]
        return self.nodes[0]
        
    def getmidseq(self, root):
        if not root:return 
        self.getmidseq(root.left)
        self.nodes.append(root)
        self.getmidseq(root.right)

#思路：二叉搜索树的中序是有序的，左子树（如果有）的最右结点和根结点连接， 右子树（如果有）的最左结点和根连接。递归实现
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution2:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:return 
        def cc(pRootOfTree):
            if not pRootOfTree: return
            #print('pRootOfTree:'+str(pRootOfTree.val))
            cc(pRootOfTree.left)
            l = pRootOfTree.left if pRootOfTree.left else None #找到左子树的最右结点
            while l:
                if l.right:
                    l = l.right
                else:break
            pRootOfTree.left = l 
            if l:
                l.right = pRootOfTree
            cc(pRootOfTree.right)
            r = pRootOfTree.right if pRootOfTree.right else None #找到右子树的最左结点
            while r:
                if r.left:
                    r = r.left
                else:break
            pRootOfTree.right = r 
            if r:
                r.left = pRootOfTree
            return  #测试时，这个return可以不写，因为修改是在原结点上进行的，无需返回值
        cc(pRootOfTree)
        head = pRootOfTree
        while head.left:
            head = head.left
        return head


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

a = TreeNode(9);b = TreeNode(11);c=TreeNode(6);d=TreeNode(3);e=TreeNode(8);f=TreeNode(7)
a.left=c;a.right=b;c.left=d;c.right=e;e.left=f;head=a 
def midseq(root):
    if root.left:
        midseq(root.left) #因为函数无返回值，只是打印，所以可不写return
    if root.right:
        midseq(root.right)
midseq(a)  