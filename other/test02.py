'''
@Time    : 2020/4/29 11:13
@FileName: 08-08test02.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''
import sys


def f(n):
    if n == 1:
        return 3
    res = 2 * f(n - 1) + 1
    return res


if __name__ == '__main__':
    res = f(4)
    print(res)
