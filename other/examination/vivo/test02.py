# coding=utf-8
# -*- coding:utf-8 -*-
'''
Author: Solarzhou
Email: t-zhou@foxmail.com

date: 2020/6/7 15:55
desc:
'''


def test02():
    n = int(input().strip())
    res = []
    for i in range(n):
        temp = input().strip().split()
        temp = list(map(int, temp))
        res.extend(temp)
    res.sort()
    for i in res:
        print(i, end=" ")


if __name__ == '__main__':
    test02()
