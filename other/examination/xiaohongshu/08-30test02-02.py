# coding=utf-8
# -*- coding:utf-8 -*-
'''
Author: Solarzhou
Email: t-zhou@foxmail.com

date: 2020/8/30 20:09
desc:
'''


def maxBoxes():
    _boxes_rows = int(input())
    _boxes_cols = int(input())

    _boxes = []
    for _boxes_i in range(_boxes_rows):
        _boxes_temp = list(map(int, input().strip().split(" ")))
        _boxes.append(_boxes_temp)
    res1, res2 = 1, 1
    temp1 = sorted(_boxes, key=lambda x: (x[0], x[1]))
    # print(temp1)
    first, second = temp1[0][0], temp1[0][1]
    index1 = 0
    for i in range(1, _boxes_rows):
        if temp1[i][0] <= first and temp1[i][1] <= second:
            first = temp1[i][0]
            second = temp1[i][1]
            index1 = i

    for i in range(0, _boxes_rows):
        if temp1[i][0] > first and temp1[i][1] > second:
            res1 += 1
            first = temp1[i][0]
            second = temp1[i][1]
    ## res3
    first, second = temp1[1][0], temp1[1][1]
    index1 = 0
    res3 = 0
    for i in range(1, _boxes_rows):
        if temp1[i][0] <= first and temp1[i][1] <= second:
            first = temp1[i][0]
            second = temp1[i][1]
            index1 = i

    for i in range(0, _boxes_rows):
        if temp1[i][0] > first and temp1[i][1] > second:
            res1 += 1
            first = temp1[i][0]
            second = temp1[i][1]

    temp2 = sorted(_boxes, key=lambda x: (x[1], x[0]))
    # print(temp2)
    first, second = temp2[0][0], temp2[0][1]
    index1 = 0
    for i in range(1, _boxes_rows):
        if temp2[i][0] <= first and temp2[i][1] <= second:
            first = temp2[i][0]
            second = temp2[i][1]
            index1 = i

    for i in range(0, _boxes_rows):
        if temp2[i][0] > first and temp2[i][1] > second:
            res2 += 1
            first = temp2[i][0]
            second = temp2[i][1]
    return max(res1, res2, res3)


# ******************************结束写代码******************************


if __name__ == '__main__':
    res = maxBoxes()
    print(res)
