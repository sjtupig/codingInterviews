# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        '''
        本质上来说，这还是一个有序系列的查找问题------所以用二分查找法
        另外有几个边界情况，1、未旋转
                          2、二分查找时low==mid==high
                          3、另外while用rotateArray[low] >= rotateArray[high]而不是用low<=high则省去了在循环体中对两端大小判断，使得代码更简洁
        '''
        if not rotateArray:
            return 0
        if rotateArray[0] < rotateArray[-1]:
            return rotateArray[0]
        low, high = 0, len(rotateArray)-1
        while rotateArray[low] >= rotateArray[high]:
            if low+1==high:
                return rotateArray[high]
            mid = int((low+high)/2)
            if rotateArray[low] == rotateArray[mid] == rotateArray[high]:
                for i in range(low, high-1):
                    if rotateArray[i] > rotateArray[i+1]:
                        return rotateArray[i+1]
            if rotateArray[low] <= rotateArray[mid]:
                low = mid
            if rotateArray[high] >= rotateArray[mid]:
                high = mid
            