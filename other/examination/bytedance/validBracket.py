'''
@Time    : 2020/3/31 22:27
@FileName: validBracket.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution:
    # 有效括号
    # 使用栈来处理,符合要求的加入栈中，不符合要求的弹出
    # 最后判断栈的长度是否为零
    def isValid(self, s):
        if not s:
            return True
        sLen = len(s)
        stack = []
        for i in range(sLen):
            c = s[i]
            if c == '(':
                stack.append(c)
            elif not stack:
                return False
            else:
                stack.pop()
        return len(stack) == 0

    # 上述时间复杂度为O(n),空间复杂度也为O(n),
    # 下面通过常数统计“（”的数目来进行空间优化
    def isValid2(self, s):
        if not s:
            return True
        sLen = len(s)
        count = 0
        for i in range(sLen):
            c = s[i]
            if c == '(':
                count += 1
            elif count == 0:
                return False
            else:
                count -= 1
        return count == 0
