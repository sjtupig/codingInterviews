
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        def dfs(root, expectNumber):
            temp.append(root.val)
            if sum(temp) == expectNumber and not root.left and not root.right:
                res.append(temp[:])  #这里必须使用temp[:]， 使用temp失败， a[:] 是深复制 ，在python的赋值中，是通过对象的地址引用进行的赋值，a[:]修改的是堆中的内容，意思是指针还指向这里
            if root.left:
                dfs(root.left, expectNumber)
            if root.right:
                dfs(root.right, expectNumber)
            temp.pop()
        if not root:
            return []
        res, temp = [],[]
        dfs(root, expectNumber)
        return res

################################################################################################################################

#先深度优先找到所有路径
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        res=[]
        treepath=self.dfs(root)
        for i in treepath:
            if sum(map(int,i.split('->')))==expectNumber:
                res.append(list(map(int,i.split('->'))))
        return res
 
    def dfs(self, root):
        if not root: return []
        if not root.left and not root.right:
            return [str(root.val)]
        treePath = [str(root.val) + "->" + path for path in self.dfs(root.left)]
        treePath += [str(root.val) + "->" + path for path in self.dfs(root.right)]
        return treePath


class Solution:
    def FindPath(self, root, expectNumber):
        return [map(int, i.split("->")) for i in self.dfs(root) if sum(map(int, i.split('->'))) == expectNumber]
    def dfs(self, root):
        if not root: return []
        if not root.left and not root.right: return [str(root.val)]
        treePath = [str(root.val) + "->" + path for path in self.dfs(root.left)]
        treePath += [str(root.val) + "->" + path for path in self.dfs(root.right)]
        return treePath

#记忆深度dfs

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
 
        self.list = []
        self.list1 = []
    def FindPath(self, root, expectNumber):
        if root == None:
            return self.list1
        # print('********')
        self.list.append(root.val)
        # print(list)
        expectNumber -= root.val
        # print('----', target)
        if expectNumber == 0 and root.left == None and root.right == None:
            newlist = []
            for line in self.list:
                newlist.append(line)
            self.list1.append(newlist)
        # print('*****', list1)
        # list1.append(proot.val)
        # print(list1)
        # print(list)
        # print('********')
        # print(proot.val)
        # print('********')
 
        self.FindPath(root.left, expectNumber)
 
        self.FindPath(root.right, expectNumber)
        self.list.pop()
        return self.list1




class Solution:
    def FindPath(self, root, expectNumber):
        def subFindPath(root):
            if root:
                b.append(root.val)
                if not root.right and not root.left and sum(b) == expectNumber:
                    a.append(b[:])
                else:
                    subFindPath(root.left),subFindPath(root.right)
                b.pop()
        a, b = [], []
        subFindPath(root)
        return a


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        def dfs(root, expectNumber):
            temp.append(root.val)
            if sum(temp) == expectNumber & not root.left and not root.right:
                res.append(temp[:])
            if root.left:
                dfs(root.left, expectNumber)
            if root.right:
                dfs(root.right, expectNumber)
            temp.pop()
        
        res, temp = [],[]
        dfs(root, expectNumber)
        return res
        