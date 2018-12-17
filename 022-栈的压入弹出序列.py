def IsPopOrder(pushV, popV):
        # write code here
        
        a = []#辅助栈，模拟入栈出栈
        j = 0
        for i in pushV:
            a.append(i)
            while a and  a[-1] == popV[j]:
                a.pop()
                j += 1
        if j == len(popV):
            return True
        return False

pushV = [1,2,3,4,5]
popV = [4,3,5,1,2]
print(IsPopOrder(pushV, popV))