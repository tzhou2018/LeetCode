'''
@Time    : 2020/3/18 11:25
@FileName: lowestCommonMultiple.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution:
    # 最小公倍数为两数的乘积除以最大公约数。
    def minCommonMultiple(self, m, n):
        return m * n / self.maxCommonDivisor(m, n)
    # 求最大公约数
    def maxCommonDivisor(self, m, n):
        return m if n == 0 else self.maxCommonDivisor(n, m % n)


if __name__ == '__main__':
    print(Solution().minCommonMultiple(12, 16))
    print(Solution().maxCommonDivisor(12, 16))
