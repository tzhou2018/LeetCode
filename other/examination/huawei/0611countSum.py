# coding=utf-8
# -*- coding:utf-8 -*-
'''
Author: Solarzhou
Email: t-zhou@foxmail.com

date: 2020/6/11 14:13
desc:
'''
"""
6.11 号笔试：
给定一个数字N，求组合数和为N的正整数个数。
"""


def countSum(candidates, n):
    res = []

    def recursion(candidates, n, curList, index):
        if n < 0:
            return
        if 0 == n:
            res.append(curList)
        for i in range(index, len(candidates)):
            recursion(candidates, n - candidates[i], curList + [candidates[i]], i)

    recursion(candidates, n, [], 0)
    return res


class Solution:
    res = 0

    def recursion(self, n, j, sum):
        if sum > n:
            return
        if sum == n:
            self.res += 1
            return
        for i in range(j, n + 1):
            self.recursion(n, i, sum + i)

    def getRes(self, n):
        self.recursion(n, 1, 0, )
        return self.res

    def recursion2(self, arr, index, aim):
        res = 0
        if (index == len(arr)):
            res = 1 if aim == 0 else 0
        else:
            for i in range(len(arr) + 1):
                if i * arr[index] <= aim:
                    res += self.recursion2(arr, index + 1, aim - arr[index] * i)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.getRes(4))
    print(solution.recursion2([1, 2, 3, 4], 0, 4))
    print(countSum([1, 2, 3, 4], 4))
