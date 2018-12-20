#暴力解法
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
    
#最优解法

'''
不是比较a和b，而是比较ab与 ba。如果ab < ba，则a < b；如果ab > ba，则a > b；如果ab = ba，则a = b。
比较函数的定义是本解决方案的关键。这道题其实就是希望我们能找到一个排序规则，根据这个规则排出来的数组能排成一个最小的数字。
sorted()也是一个高阶函数，它可以接收一个比较函数来实现自定义排序，比较函数的定义是，
传入两个待比较的元素 x, y，如果 x 应该排在 y 的前面，返回 -1，如果 x 应该排在 y 的后面，
返回 1。如果 x 和 y 相等，返回 0
'''
# -*- coding:utf-8 -*-
from itertools import permutations
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:return ''
        numbers = [str(i) for i in numbers]
        def my_cmp(x, y):
            if x+y < y+x:
                return -1
            elif x+y > y+x:
                return 1
            else:
                return 0
        s_n_sorted = sorted(numbers, cmp = my_cmp)
        return ''.join(s_n_sorted)
