# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#哈希表法
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        hashtable = {}
        while pHead:
            if pHead in hashtable:
                return pHead
            else:
                hashtable[pHead] = 1
            pHead = pHead.next
        return None

class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        slow,fast=pHead,pHead
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                slow2=pHead
                while slow!=slow2:
                    slow=slow.next
                    slow2=slow2.next
                return slow

'''
链接：https://www.nowcoder.com/questionTerminal/253d2c59ec3e4bc68da16833f79a38e4
来源：牛客网

//左神讲的
//先说个定理：两个指针一个fast、一个slow同时从一个链表的头部出发
//fast一次走2步，slow一次走一步，如果该链表有环，两个指针必然在环内相遇
//此时只需要把其中的一个指针重新指向链表头部，另一个不变（还在环内），
//这次两个指针一次走一步，相遇的地方就是入口节点。
//这个定理可以自己去网上看看证明。

'''

#双指针
'''
受到第15题的启发剑指Offer--015-链表中倒数第k个结点, 我们考虑这样一个事实

假设链表长度为N, 那么第N链接到了第k个节点形成了环，即我们需要查找到倒数第N-K+1个节点, 那么环中就有N-K+1个节点，这时候我们定义两个指针$P_1$和$P_2$指向链表的头部, 
指针$P_1$先在链表中向前移动n-k+1步,到达第n-k+2个节点, 然后两个指针同步向前移动, 当$P_2$走了K-1步到达环的入口的时候, 指针$P_1$正好走了N+1步, 到达了环的入口, 即两个指针会相遇在环的入口处

那么我们剩下的问题就是如何得到环中节点的数目?

我们可以使用一快一慢两个指针（比如慢指针一次走一步，　慢指针一次走两步），如果走的过程中发现快指针追上了慢指针, 说明遇见了环，
而且相遇的位置一定在环内, 考虑一下环内, 从任何一个节点出现再回到这个节点的距离就是环的长度, 于是我们可以进一步移动慢指针，快指针原地不动, 
当慢指针再次回到相遇位置时, 正好在环内走了一圈, 从而我们通过计数就可以获取到环的长度

第一步，找环中相汇点。分别用p1，p2指向链表头部，p1每次走一步，p2每次走二步，直到p1==p2找到在环中的相汇点。

第二步，找环的长度。从环中的相汇点开始, p2不动, p1前移，　当再次相遇时，p1刚好绕环一周, 其移动即为环的长度K

第三步, 求换的起点, 转换为求环的倒数第N-K个节点，则两指针left和right均指向起始, right先走K步, 然后两个指针开始同步移动, 当两个指针再次相遇时, right刚好绕环一周回到起点, left则刚好走到了起点位置'''

'''
#断链法
时间复杂度为O（n），两个指针，一个在前面，另一个紧邻着这个指针，在后面。 两个指针同时向前移动，每移动一次，前面的指针的next指向NULL。 
也就是说：访问过的节点都断开，最后到达的那个节点一定是尾节点的下一个， 也就是循环的第一个。 这时候已经是第二次访问循环的第一节点了，第一次访问的时候我们已经让它指向了NULL， 所以到这结束。
'''