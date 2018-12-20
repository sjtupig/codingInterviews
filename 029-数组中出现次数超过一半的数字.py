#方法一：朴素实现，哈希表记录每个元素的个数
#pass

#方法二：
# -*- coding:utf-8 -*-
#特点--它出现的次数比其他所有的数组出现的次数之和还要多
class Solution1:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        stack = []
        for i in numbers:
            if stack:
                if i != stack[-1]:
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        if not stack:return 0 
        cnt = 0
        for i in numbers:
            if i == stack[-1]:
                cnt += 1

        return stack[-1] if cnt > len(numbers)/2 else 0
#方法三
'''数组中有一个数字出现的次数超过了数组长度的一半，那么如果我们把这个数组排序，那么排序之后位于数组中间的那个数字一定就是那个出现次数超过数组长度一半的数字

也就是说这个数字其实就是统计学上的中位数，即长度为N的数组中的$N/2$大的元素，因此我们的题目最后成为返回数组中第K（$K=Len/2$）大的数。

因此我们的问题成为查找一个数组中的K大的元素
https://blog.csdn.net/xiaoding133/article/details/8037086
http://blog.chinaunix.net/uid-20196318-id-189514.html

'''
# -*- coding:utf-8 -*-
class Solution2:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        numbers.sort()
        if len(numbers)%2:
            num_candidate = numbers[int(len(numbers)/2)]
        else:
            if numbers[len(numbers)/2] != numbers[len(numbers)/2-1]:
                return 0
            else:
                num_candidate = numbers[len(numbers)/2]
        cnt = 0
        for i in numbers:
            if i == num_candidate:
                cnt += 1 

        return num_candidate if cnt > len(numbers)/2 else 0

#使用collections中的Counter
# -*- coding:utf-8 -*-
from collections import Counter
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        a = Counter(numbers)
        for key, value in a.items():
            if value > len(numbers)/2:
                return key
        return 0



numbers = [1,2,3,2,2,2,5,4,2]
sol = Solution2()
print(sol.MoreThanHalfNum_Solution(numbers))