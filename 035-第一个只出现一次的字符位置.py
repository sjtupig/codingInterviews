#哈希表法
# -*- coding:utf-8 -*-
from collections import Counter
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        char_nums = Counter(s)
        for i in range(len(s)):
            if char_nums[s[i]] == 1:
                return i
        return -1


#bitmap方法-同计数法，略微有变动
'''我们计数数组不简单的存储计数

只出现一次的字符会存储出现的位置
出现多次的字符就存储标识-1 因此查找数组中非-1的最小值即可'''