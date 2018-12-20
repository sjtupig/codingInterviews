# -*- coding:utf-8 -*-
from itertools import permutations
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:return ''
        numbers = [str(i) for i in numbers]
        c_numbers = [list(i) for i in permutations(numbers)]
        strs = [''.join(i) for i in c_numbers]
        return min(strs)