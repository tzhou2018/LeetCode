# coding=utf-8
# -*- coding:utf-8 -*-
'''
Author: Solarzhou
Email: t-zhou@foxmail.com

date: 2020/8/30 20:49
desc:
'''


def test03():
    arr = list(map(int, input().strip().split(" ")))
    rows = arr[0]
    cols = arr[1]
    matrix = []
    r = arr[2]
    c = arr[3]
    for i in range(rows):
        matrix.append(list(map(int, input().strip().split(" "))))
    return r * c


if __name__ == '__main__':
    res = test03()
    print(res)
