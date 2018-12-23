# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        return data.count(k)


# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        cnt = 0
        if_count = False
        for i in data:
            if if_count and i != k:
                return cnt
            if i == k:
                cnt += 1
                if_count = True
        return cnt



#由于数组是有序的，这时候可以考虑二分查找。先找到k的位置，然后向前向后遍历
# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        l, r = 0, len(data)-1
        index_k = -1
        while l < r:
            mid = int((l+r)/2)
            #print('l:',l,'mid:',mid,'r:',r)
            if data[mid] == k:
                index_k = mid
                break 
            if data[mid] < k:
                l = mid+1
            if data[mid] > k:
                r = mid-1
        cnt = 0
        s_l = index_k
        while s_l >= 0 and data[s_l] == k:
            cnt += 1
            s_l -= 1
        s_r = index_k+1
        while s_r < len(data) and data[s_r] == k:
            cnt += 1
            s_r += 1
        return cnt

data = [1,2,3,3,3,4,4,6]
k = 4
sol = Solution()
print(sol.GetNumberOfK(data, k))