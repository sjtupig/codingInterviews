# -*- coding:utf-8 -*-
#这里计算的是结点的个数
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        #统计结点的个数，最后-1
        self.max_len = 0
        self.node_nums = 0
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:return 0
        self.node_nums += 1
        if pRoot:
            print('pRoot.val',pRoot.val)
        print('self.node_nums',self.node_nums)
        if not pRoot.left and not pRoot.right:
            self.max_len = max(self.max_len, self.node_nums)
        if pRoot.left:
            self.TreeDepth(pRoot.left)
            self.node_nums -=1
        if pRoot.right:
            self.TreeDepth(pRoot.right)
            self.node_nums -= 1
            
        return self.max_len



# 方法2：使用递归
        # 如果该树只有一个结点，它的深度为1.如果根节点只有左子树没有右子树，
        # 那么树的深度为左子树的深度加1；同样，如果只有右子树没有左子树，
        # 那么树的深度为右子树的深度加1。如果既有左子树也有右子树，
        # 那该树的深度就是左子树和右子树的最大值加1.
class Solution:
    def TreeDepth(self, pRoot):
        if pRoot==None:return 0
        return max(self.TreeDepth(pRoot.left),self.TreeDepth(pRoot.right))+1


#除此以外，还可以用层次遍历的方法来写，这里用队列来做，，前面写过类似代码，后面有时间再补

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)
h = TreeNode(8)
'''a.left = b
 a.right = c 
 b.left = d
 b.right = e 
 e.left = g 
 c.right = f 
 f.right = h''' 
a.right = b
b.right = c 
c.right = d 
d.right = e 

sol = Solution()
print(sol.TreeDepth(a))
