# coding=utf-8
# -*- coding:utf-8 -*-
'''
Author: Solarzhou
Email: t-zhou@foxmail.com

date: 2020/6/7 15:22
desc:
'''


def Flowers():

    n = int(input().strip())
    flowerbed = input().strip().split()[:n]
    flowerbed = list(map(int, flowerbed))
    res = 0
    lenFlo = len(flowerbed)
    for i in range(lenFlo):
        if flowerbed[i] == 1:
            continue
        pre = 0 if i == 0 else flowerbed[i - 1]
        next = 0 if i == lenFlo - 1 else flowerbed[i + 1]
        if pre == 0 and next == 0:
            res += 1
            flowerbed[i] = 1
    return res


if __name__ == '__main__':
    res = Flowers()
    print(res)
