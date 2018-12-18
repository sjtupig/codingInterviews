# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        m, n = len(matrix), len(matrix[0])#row数，col数
        print(m)
        print(n)
        r_low, r_high, c_low, c_high = 0, m-1, 0, n-1#遍历时，行列的边界
        i,j = 0,0 #行列起始点
        res = [] 
        while True:
            while j <= c_high:
                #print('add i:'+str(i)+',j:'+str(j))
                res.append(matrix[i][j])
                if len(res) == m*n:
                    return res
                j += 1
            i += 1  #别忘了向下一步
            j-= 1  #跳出while循环j多减了一次，加回来
            while i <= r_high:
                #print('add i:'+str(i)+',j:'+str(j))
                res.append(matrix[i][j])
                if len(res) == m*n:
                    return res
                i += 1
            j -= 1 #向左一步
            i -= 1
            while j >= c_low:
                #print('add i:'+str(i)+',j:'+str(j))
                res.append(matrix[i][j])
                if len(res) == m*n:
                    return res
                j -= 1
            i -= 1
            j += 1
            while i > r_low:
                #print('add i:'+str(i)+',j:'+str(j))
                res.append(matrix[i][j])
                if len(res) == m*n:
                    return res
                i -= 1
            r_low += 1
            r_high -= 1
            c_low += 1
            c_high -= 1
            j += 1
            i += 1

matrix1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
matrix3 = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
so = Solution()
print(so.printMatrix(matrix2))
print(so.printMatrix(matrix2))
print(so.printMatrix(matrix3))