# -*- coding:utf-8 -*-
from collections import OrderedDict  #有序字典
class Solution:
    # 返回对应char
    def __init__(self):
        self.char_nums = OrderedDict()
    def FirstAppearingOnce(self):
        # write code here
        if not self.char_nums: return '#'
        for key, val in self.char_nums.items():
            if val == 1:
                return key
        return '#'
    def Insert(self, char):
        # write code here
        if char in self.char_nums:
            self.char_nums[char] += 1
        else:
            self.char_nums[char] = 1