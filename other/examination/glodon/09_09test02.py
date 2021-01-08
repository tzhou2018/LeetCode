"""
@Time       : 2020/9/9 20:58
@FileName   : 09_09test02.py
@Author     : Solarzhou
@Email      : t-zhou@foxmail.com
"""

import math


def test02():
    n, w = list(map(int, input().strip().split(" ")))
    vals = []
    wts = []
    for i in range(n):
        temp = input().strip().split(" ")
        if float(temp[0]) > w:
            continue
        wts.append(math.ceil(float(temp[0])))
        vals.append(int(temp[1]))
    # if not vals or not wts:
    #     return 0
    n = len(wts)
    dp = [[0] * (w + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, w + 1):
            if j - wts[i - 1] < 0:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - (wts[i - 1])] + vals[i - 1])
    # for i in range(n + 1):
    #     print(dp[i])
    # print(dp)
    return dp[n][w]


# class Node:
#     def __init__(self, c, w):
#         self.c = c
#         self.w = w
#
#
# import functools
#
#
# # 比较器
# def maxComparator(o1, o2):
#     return o2.w - o1.w
#
#
# def test021():
#     n, c = list(map(int, input().strip().split(" ")))
#     # vals = []
#     # wts = []
#     nodes = []
#     for i in range(n):
#         temp = input().strip().split(" ")
#         # wts.append(float(temp[0]))
#         # vals.append(int(temp[1]))
#         if float(temp[0]) <= c:
#             nodes.append(Node(float(temp[0]), int(temp[1])))
#
#     # nodes.sort(key=functools.cmp_to_key(maxComparator))
#     nodes = sorted(nodes, key=functools.cmp_to_key(maxComparator))
#     res = 0
#     while nodes and nodes[0].c <= c:
#         temp = nodes.pop(0)
#         res += temp.w
#         c -= temp.c
#
#     # print(res)
#
#     return res


if __name__ == '__main__':
    res = test02()
    print(res)
