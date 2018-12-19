#四种方法

#第一种，递归实现， 但是这种实现实际上来说是不对的，因为new链表的random指向的是原来链表的random，耦合在了一起，可以看最后面的测试代码

# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution1:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return 
        newhead = RandomListNode(pHead.label)
        newhead.random = pHead.random
        newhead.next = self.Clone(pHead.next)
        return newhead
#第二种 哈希表
class Solution2:
    def Clone(self, head):
        nodeList = []     #存放各个节点
        randomList = []   #存放各个节点指向的random节点。没有则为None
        labelList = []    #存放各个节点的值
        while head:
            randomList.append(head.random)
            nodeList.append(head)
            labelList.append(head.label)
            head = head.next
        #random节点的索引，如果没有则为1   
        labelIndexList = map(lambda c: nodeList.index(c) if c else -1, randomList)  #这个很巧妙
        
        dummy = RandomListNode(0)
        pre = dummy
        #节点列表，只要把这些节点的random设置好，顺序串起来就ok了。
        nodeList=map(lambda c:RandomListNode(c),labelList)
        #把每个节点的random绑定好，根据对应的index来绑定
        for i in range(len(nodeList)):
            if labelIndexList[i]!=-1:
                nodeList[i].random=nodeList[labelIndexList[i]]
        for i in nodeList:
            pre.next=i
            pre=pre.next
        return dummy.next
#第三种：三步走法
class Solution3:
    def Clone(self, pHead):
        #第一步，在每个节点后面插入一个复制的新节点
        t = pHead
        while t:
            node = RandomListNode(t.label)
            node.next = t.next
            t.next = node 
            t = t.next.next #t = node.next
        #第二步，把random指针加上去
        t = pHead
        while t:
            t.next.random = t.random.next if t.random else None
            t = t.next.next 
        #第三步，拆分,插入，
        #初始化
        newpHead = pHead.next
        pHead.next = newpHead.next
        #newpHead.next = None
        node = newpHead
        rawpHead = pHead.next
        while rawpHead:
            node.next = rawpHead.next
            node = node.next
            rawpHead.next = node.next
            rawpHead = rawpHead.next
        return newpHead

#第四种：deepcopy
import copy
class Solution4:
    # 返回 RandomListNode
    def Clone(self, pHead):
        
        return copy.deepcopy(pHead)
'''
直接赋值：其实就是对象的引用（别名）。

浅拷贝(copy)：拷贝父对象，不会拷贝对象的内部的子对象。

深拷贝(deepcopy)： copy 模块的 deepcopy 方法，完全拷贝了父对象及其子对象。 
参考: 

https://docs.python.org/2/library/copy.html

http://www.runoob.com/w3cnote/python-understanding-dict-copy-shallow-or-deep.html
关于deepcopy这个博客也解释的很详细

https://blog.csdn.net/qq_32907349/article/details/52190796



'''
#测试代码
class RandomListNode:
     def __init__(self, x):
            self.label = x
            self.next = None
            self.random = None

a = RandomListNode(1)
b = RandomListNode(2)
c = RandomListNode(3)
d = RandomListNode(4)
a.next = b
b.next = c
c.next = d
a.random = c
b.random = d
c.random = b
d.random = a
head = a

sol = Solution3()
res = sol.Clone(head)
print('lianbiao')
print(head.label)
print(head.next.label)
print(head.next.next.label)
print(head.next.next.next.label)
print('lianbiao_random')
print(head.random.label)
print(head.next.random.label)
print(head.next.next.random.label)
print(head.next.next.next.random.label)
print('newlianbiao')
print(res.label)
print(res.next.label)
print(res.next.next.label)
print(res.next.next.next.label)
print('newlianbiao_random')
print(res.random.label)
print(res.next.random.label)
print(res.next.next.random.label)
print(res.next.next.next.random.label)

#一下为markdown文件内容
'''

```python
class RandomListNode:
     def __init__(self, x):
            self.label = x
            self.next = None
            self.random = None
```


```python
a = RandomListNode(1)
```


```python
b = RandomListNode(2)
```


```python
c = RandomListNode(3)
```


```python
d = RandomListNode(4)
```


```python
a.next = b
```


```python
b.next = c
```


```python
c.next = d
```


```python
a.random = c
```


```python
b.random = d
```


```python
c.random = b
```


```python
d.random = a
```


```python
a.random.label
```




    3




```python
id(a)
```




    1944757342616




```python
id(b)
```




    1944757342784




```python
id(c)
```




    1944757343512




```python
phead = a
```


```python
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return 
        newhead = RandomListNode(pHead.label)
        newhead.random = pHead.random
        newhead.next = self.Clone(pHead.next)
        return newhead
```


```python
sol = Solution()
```


```python
newhead = sol.Clone(phead)
```


```python
newhead.label, phead.label
```




    (1, 1)




```python
newhead.random.label, phead.random.label
```




    (3, 3)




```python
id(newhead.random), id(phead.random)
```




    (1944757343512, 1944757343512)




```python
id(newhead.next), id(phead.next)
```




    (1944758000272, 1944757342784)




```python

```

'''
