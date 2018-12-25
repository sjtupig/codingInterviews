# -*- coding:utf-8 -*-
#这题同样可以用字符串翻转来做

#这种题为：外部大顺序逆序，内部小顺序不逆序，可以用二次翻转来做
class Solution:
    def ReverseSentence(self, s):
        # write code here
        def reverse(a):
            l, r = 0, len(a)-1
            while l < r:
                a[l],a[r] = a[r],a[l]
                l+=1
                r-=1
            return a
        words = s.split(' ')
        for i, val in enumerate(words):
            words[i] = ''.join(reverse(list(val)))
        return ''.join(reverse(list(' '.join(words))))


class Solution:
    def ReverseSentence(self, s):
        # write code here
        def reverse(a):
            l, r = 0, len(a)-1
            while l < r:
                a[l],a[r] = a[r],a[l]
                l+=1
                r-=1
            return a
        words = s.split(' ')
        words_new = []
        for i in words:#这里遍历方法不能直接修改list，可以使用下标遍历的办法
            words_char = list(i)
            words_new.append(''.join(reverse(words_char)))
        return ''.join(reverse(list(' '.join(words_new))))
sol = Solution()
s = 'student. a am I'
print sol.ReverseSentence(s)