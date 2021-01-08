# coding=utf-8
# -*- coding:utf-8 -*-
'''
Author: Solarzhou
Email: t-zhou@foxmail.com

date: 2020/6/15 20:33
desc:
'''


def moveXP(x, y, m):
    return x + m, y


def moveXN(x, y, m):
    return x - m, y


def moveYP(x, y, m):
    return x, y + m


def moveYN(x, y, m):
    return x, y - m

# 没时间写咯
def fun2():
    n = int(input().strip())
    res = []
    for i in range(n):
        res.append(list(map(int, input().strip().split())))
    x, y = 0, 0
    for e in res:
        if e[0] == 1 and e[1] > 0:
            x, y = moveXP(x, y, e[1])
        if e[0] == -1 and e[1] > 0:
            x, y = moveXN(x, y, e[1])
        if e[0] == 2 and e[1] > 0:
            x, y = moveYP(x, y, e[1])
        if e[0] == -2 and e[1] > 0:
            x, y = moveYN(x, y, e[1])
    if (x, y) == (18, 18):
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    print(fun2())
