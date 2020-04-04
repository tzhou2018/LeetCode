'''
@Time    : 2020/3/18 10:48
@FileName: 204countPrimes.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


# 方法1
# 常规做法，遍历所给数字，逐个判断每一数字
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(2, n):
            if self.isPrime(i):
                count += 1
        return count

    def isPrime(self, m):
        i = 2
        while i * i <= m:
            if m % i == 0:
                # 有其他因子
                return False
            i += 1
        return True


# 方法2
# 对之前的算法进行优化
# 首先从 2 开始，我们知道 2 是一个素数，
# 那么 2 × 2 = 4, 3 × 2 = 6, 4 × 2 = 8... 都不可能是素数了。

# 然后我们发现 3 也是素数，那么 3 × 2 = 6, 3 × 3 = 9, 3 × 4 = 12...
# 也都不可能是素数了。
class Solution2(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        isPrime = [True] * n
        # 外层循环还能在优化 判断条件设为 i * i < n
        for i in range(2, n):
            if isPrime[i]:
                for j in range(i * i, n, i):
                    isPrime[j] = False
        for i in range(2, n):
            if isPrime[i]:
                count += 1
        return count
