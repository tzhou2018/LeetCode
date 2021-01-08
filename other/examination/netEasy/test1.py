'''
@Time    : 2020/4/25 10:16
@FileName: test1.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


def fun1():
    str1 = input().strip()
    start = 1
    end = len(str1)
    count = 1
    res = ""
    while end > start:
        if str1[start] != str1[start - 1]:
            res += str(count) + str1[start - 1]
            count = 1
            start += 1
        else:
            start += 1
            count += 1
    return res + str(count) + str1[start - 1]


if __name__ == '__main__':
    print(fun1())
