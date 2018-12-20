#方法一：使用库函数 排列和组合的函数
#要注意去重 和 排序
from itertools import permutations
class Solution1:
    def Permutation(self, ss):
        # write code here
        if not ss:return []
        charlist = [i for i in ss]
        res = [list(i) for i in list(permutations(charlist))]
        res = [''.join(i) for i in res]
        res = list(set(res))
        res.sort()
        return res

#方法二：拼接

class Solution2:
    def Permutation(self, ss):
        nums = [i for i in ss]
        nums.sort()#每次有新数来，是插入当前已有的每个位置比如 已有 [1,2],[2,1], 3就是插入每个空位，[3,1,2],[1,3,2],[1,2,3],[3,2,1],[2,3,1],[2,1,3]
        n = len(nums)
        res = []
        now_res = [] #当前结果
        for i in nums:
            now_res = []
            if res != []:
                for j in res:
                
                    for k in range(len(j)+1):
                        tp = []
                        if k == 0:
                            tp.append(i)
                            tp.extend(j)
                        else:
                            tp.extend(j[0:k])
                            tp.append(i)
                            tp.extend(j[k:])
                        now_res.append(tp)
            else:
                now_res = [[i]]
            res = now_res
        res = [''.join(i) for i in res]
        res = list(set(res))
        res.sort()
        return res








ss = ''
sol = Solution2()
print(sol.Permutation(ss))