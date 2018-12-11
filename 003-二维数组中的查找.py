def arrays_search(target, array):
    #如果从左上角开始搜索，那么右边和下边两个方向都是增大，没有减小，而从右上角开始搜索，往左是减小，往下是增大，if else很明显
    m, n = len(array), len(array[0])
    j = n-1
    i = 0 
    
    while 0 <= j < n and 0 <= i < m:
        if array[i][j] == target:
            return True
        if array[i][j] < target:
            i += 1
            continue 
        if array[i][j] > target:
            j -= 1
            continue

    return False 

a = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
res = arrays_search(5, a)
print(res)