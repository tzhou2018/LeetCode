"""
@Time       : 2020/9/15 19:25
@FileName   : 09_15test01.py
@Author     : Solarzhou
@Email      : t-zhou@foxmail.com
"""


def test01():
    while True:
        s = input().strip()
        res = isValid(s)
        print(res)


def isValid(s):
    example = ["[]", "{}", "()"]
    stack = []
    for i in range(len(s)):
        stack.append(s[i])
        if len(stack) >= 2 and stack[-2] + stack[-1] in example:
            stack.pop()
            stack.pop()
    return "true" if len(stack) == 0 else "false"


if __name__ == '__main__':
    test01()
