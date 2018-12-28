'''
如果当前结点有右子树, 那么其中序遍历的下一个结点就是其右子树的最左结点

如果当前结点没有右子树, 而它是其父结点的左子结点那么其中序遍历的下一个结点就是他的父亲结点

如果当前结点没有右子树，而它还是其父结点的右子结点，这种情况下其下一个结点应该是当前结点所在的左子树的根, 因此我们可以顺着其父节点一直向上遍历, 直到找到一个是它父结点的左子结点的结点。

'''

# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        #有右子树，右子树的最左节点
        if not pNode:return 
        if pNode.right:
            t = pNode.right
            while t.left:
                t = t.left
            return t
        #如果当前结点没有右子树, 而它是其父结点的左子结点那么其中序遍历的下一个结点就是他的父亲结点
        elif pNode.next and pNode.next.left == pNode:
            return pNode.next
        #如果当前结点没有右子树，而它还是其父结点的右子结点，这种情况下其下一个结点应该是当前结点所在的左子树的根, 因此我们可以顺着其父节点一直向上遍历, 直到找到一个是它父结点的左子结点的结点。
        elif pNode.next and pNode.next.right == pNode:
            while pNode.next and pNode.next.right == pNode:
                pNode = pNode.next
            return pNode.next


'''
思路，如果这道题是求中序遍历，肯定很简单。所以我们先写一个中序遍历的算法。关键是从根节点开始遍历，所以第一步还是找到某个节点的根节点，方法是一直使用next判断即可。
再将从根节点中序遍历的结果保存到一个数组中，直接找pNode所在索引的下一个即可。当然要考虑这个节点是不是最后一个，如果是最后一个，直接返回None。'''   
class Solution:
    def GetNext(self, pNode):
        # write code here
        dummy = pNode
        while dummy.next:
            dummy = dummy.next
        self.result = []
        self.midTraversal(dummy)
        return self.result[self.result.index(pNode) + 1] if self.result.index(pNode) != len(self.result) - 1 else None
 
    def midTraversal(self, root):
        if not root: return
        self.midTraversal(root.left)
        self.result.append(root)
        self.midTraversal(root.right) 