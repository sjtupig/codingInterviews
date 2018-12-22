#牛客上会超时，这道题，下次试试非递归的归并排序
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.cnt = 0

    def InversePairs(self, data):
        # write code here
        def mergsort(data, l, r):
            if l < r:
                mid = int((l+r)/2)
                mergsort(data,l, mid)
                mergsort(data,mid+1,r)
                #print('l:',l,'r:',r,'mid:',mid)
                merge(data,l,mid, r)
            #else:return 

        def merge(data, l, mid, r):
            #global cnt
            left = [data[i] for i in range(l,mid+1)]
            right = [data[i] for i in range(mid+1,r+1)]
            '''print('before,data[l:r+1]',data[l:r+1])
            print('before,left:',left)
            print('before,right:', right)'''
            index_left,index_right=0,0
            l_len,r_len = len(left), len(right)
            t = l
            #print('l',l)
            while index_left < l_len and index_right < r_len:
                #print('index_left:',index_left,'index_right:',index_right,'left[index_left]:',left[index_left],'right[index_right]',right[index_right])
                if left[index_left] <= right[index_right]:
                    data[t] = left[index_left]
                    t += 1
                    index_left+= 1
                else:
                    self.cnt = (self.cnt%1000000007 + l_len-index_left%1000000007)%1000000007 #注意这里不是+1，事实上由于left[index_left]>right[index_right],index_left之后的数都会大于right[index_right]
                    data[t] = right[index_right]
                    t +=1
                    index_right += 1
                
                #print('self.cnt:',self.cnt)
            while index_left < l_len:
                data[t] = left[index_left]
                t+=1
                index_left+=1
            while index_right < r_len:
                data[t] = right[index_right]
                t+=1
                index_right+=1
            '''print('after,data[l:r+1]',data[l:r+1])
            print('after,left:',left)
            print('after,right:', right)'''
        

        mergsort(data, 0, len(data)-1)
        return self.cnt 

sol = Solution()
data = [4,2,5,3]
print(sol.InversePairs(data))
print(data)