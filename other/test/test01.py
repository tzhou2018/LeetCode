"""
@Time    : 2020/6/9 10:25
@FileName: test01.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""


def recursion(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3
    if n > 3:
        return recursion(n - 1) + 2


class Solution:
    res = 0

    def recursion1(self, n, j, sum):
        if sum == n:
            self.res += 1
            return
        for i in range(j, n + 1):
            self.recursion1(n, j, sum + i)


if __name__ == '__main__':
    Solution().recursion1(5, 1, 0, 0)

