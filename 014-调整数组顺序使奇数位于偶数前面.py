# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        #ans1
        res = []
        for i in array:
            if i % 2:
                res.append(i)
        for i in array:
            if i % 2 == 0:
                res.append(i)
        return res


        #此外，这一题还可以用冒泡排序的思想来做，注意要保持相对位置不变，所以不能用双指针扫描一遍，前偶后奇交换的方法来做