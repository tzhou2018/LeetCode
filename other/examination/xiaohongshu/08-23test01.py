# coding=utf-8
# -*- coding:utf-8 -*-
'''
Author: Solarzhou
Email: t-zhou@foxmail.com

date: 2020/8/30 20:13
desc:
'''

# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************
import sys


def splitMsg():
    count = 1
    Logest = 1024
    while True:
        arr = input().strip()
        # print(arr)
        if not arr:
            break
        if len(arr) < Logest:
            print("msg%d:%s" % (count, arr), end="\n")
            count += 1
        else:
            temp1 = arr.split(".")
            # str1 = temp1[0]
            for i in range(len(temp1)):
                if temp1[i]:
                    print("msg%d:%s" % (count, temp1[i].strip() + "."), end="\n")
                    count += 1


# ******************************结束写代码******************************


if __name__ == '__main__':
    splitMsg()
    # print("hello", end="\n")
    # print("jjlj")
