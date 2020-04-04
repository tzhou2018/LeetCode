'''
@Time    : 2020/3/18 11:21
@FileName: greatestCommonDivisor.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution:
    def maxCommonDivisor(self, m, n):
        return m if n == 0 else self.maxCommonDivisor(n, m % n)


if __name__ == '__main__':
    print(Solution().maxCommonDivisor(16, 12))
