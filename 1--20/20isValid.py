'''
@Time    : 2020/2/13 22:15
@FileName: 20isValid.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''

# 借助栈来判断，每出现一对符合要求的括号时将其弹出；
# 若最后 栈的长度为0，则满足要求。
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
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


if __name__ == '__main__':
    print(Solution().isValid('{{[[]]}}'))
