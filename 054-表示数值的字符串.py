
# -*- coding:utf-8 -*-
import re
class Solution:
    def isNumeric(self, s):
        return re.match(r"^[\+\-]?[0-9]*(\.[0-9]*)?([eE][\+\-]?[0-9]+)?$",s)

sol = Solution()
print sol.isNumeric('+100')
print sol.isNumeric('5e2')
print sol.isNumeric('-123')
print sol.isNumeric('3.1416')
print sol.isNumeric('-1E-16"')
print sol.isNumeric('12e')
print sol.isNumeric('1a3.14')
print sol.isNumeric('1.2.3')
print sol.isNumeric('+-5')
print sol.isNumeric('12e+4.3')


# -*- coding:utf-8 -*-
'''
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
'''
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        if len(s) <= 0:
            return False
        # 分别标记是否出现过正负号、小数点、e，因为这几个需要特殊考虑
        has_sign = False
        has_point = False
        has_e = False
        for i in range(len(s)):
            # 对于e的情况
            if s[i] == 'E' or s[i] == 'e':
                # 不同出现两个e
                if has_e:
                    return False
                # e不能出现在最后面，因为e后面要接数字
                else:
                    has_e = True
                    if i == len(s) -1:
                        return False   
            # 对于符号位的情况
            elif s[i] == '+' or s[i] == '-':
                # 如果前面已经出现过了符号位，那么这个符号位，必须是跟在e后面的
                if has_sign:
                    if s[i-1] != 'e' and s[i-1] != 'E':
                        return False
                # 如果这是第一次出现符号位，而且出现的位置不是字符串第一个位置，那么就只能出现在e后面
                else:
                    has_sign = True
                    if i > 0 and s[i-1] != 'e' and s[i-1] != 'E':
                        return False
            # 对于小数点的情况
            elif s[i] == '.':
                # 小数点不能出现两次；而且如果已经出现过e了，那么就不能再出现小数点，因为e后面只能是整数
                if has_point or has_e:
                    return False
                # 如果是第一次出现小数点，如果前面出现过e，那么还是不能出现小数点
                else:
                    has_point = True
                    if i > 0 and (s[i-1] == 'e' or s[i-1] == 'E'):
                        return False
            else:
                # 其他字符必须是‘0’到‘9’之间的
                if s[i] < '0' or s[i] > '9':
                    return False
        return True