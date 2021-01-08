'''
@Time    : 2020/4/25 13:08
@FileName: 0425test01.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''
"""
神奇的数字
"""


def fun1():
    arr = list(map(int, input().strip().split()))
    print(arr[-1] + arr[-2])


if __name__ == '__main__':
    fun1()
