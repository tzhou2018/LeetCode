'''
@Time    : 2020/3/4 10:39
@FileName: 20isValid.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):

    def isValid(self, s):
        if not s:
            return True
        example = ["[]", "{}", "()"]
        stack = []
        for i in range(len(s)):
            stack.append(s[i])
            if len(stack) >= 2 and stack[-2] + stack[-1] in example:
                stack.pop()
                stack.pop()
        return len(stack) == 0
