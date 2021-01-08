# coding=utf-8
# -*- coding:utf-8 -*-
'''
Author: Solarzhou
Email: t-zhou@foxmail.com

date: 2020/8/30 19:32
desc:
'''
import sys
import os
import re


# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************


def maxBoxes():
    input()


    _boxes_rows = int(input())
    _boxes_cols = int(input())
    aa = []
    if _boxes_cols > 2:
        return 0
    _boxes = []
    for _boxes_i in range(_boxes_rows):
        _boxes_temp = list(map(int, input().strip().split(" ")))
        _boxes.append(_boxes_temp)
    res1, res2 = 1, 1
    temp1 = sorted(_boxes, key=lambda x: (x[0], x[1]))
    # print(temp1)
    index1 = 0
    res = 0
    for i in range(_boxes_rows):
        first, second = temp1[i][0], temp1[i][1]
        count = 1
        for j in range(_boxes_rows):
            if temp1[j][0] > first and temp1[j][1] > second:
                first = temp1[j][0]
                second = temp1[j][1]
                count += 1
        res = max(res, count, 1)

    # for i in range(0, _boxes_rows):
    #     if temp1[i][0] > first and temp1[i][1] > second:
    #         res1 += 1
    #         first = temp1[i][0]
    #         second = temp1[i][1]
    #
    # temp2 = sorted(_boxes, key=lambda x: (x[1], x[0]))
    # # print(temp2)
    # first, second = temp2[0][0], temp2[0][1]
    # index1 = 0
    # for i in range(1, _boxes_rows):
    #     if temp2[i][0] <= first and temp2[i][1] <= second:
    #         first = temp2[i][0]
    #         second = temp2[i][1]
    #         index1 = i
    #
    # for i in range(0, _boxes_rows):
    #     if temp2[i][0] > first and temp2[i][1] > second:
    #         res2 += 1
    #         first = temp2[i][0]
    #         second = temp2[i][1]
    # return min(res1, res2)
    return res


# ******************************结束写代码******************************


if __name__ == '__main__':
    res = maxBoxes()
    print(res)
