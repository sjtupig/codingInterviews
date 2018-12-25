# -*- coding:utf-8 -*-
from collections import Counter

#规则：非0元素的极差（最大值最小值的差）不超过4， 非0元素不重复
#非0元素不重复
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        #元素个数需要==5
        if len(numbers) != 5:return False
        numbers.sort()
        count = Counter(numbers)
        #非0元素不重复
        for key, val in count.items():
            if key and val > 1:
                return False
        #非0元素的极差（最大值最小值的差）不超过4
        if numbers[-1]-numbers[count.get(0,0)] <= 4:
            return True
        return False

sol = Solution()
print sol.IsContinuous([1,0,3,0,5])