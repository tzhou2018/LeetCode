'''
@Time    : 2020/3/18 15:45
@FileName: gcd.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''
"""
对于 a 和 b 的最大公约数 f(a, b)，有：

如果 a 和 b 均为偶数，f(a, b) = 2*f(a/2, b/2);
如果 a 是偶数 b 是奇数，f(a, b) = f(a/2, b);
如果 b 是偶数 a 是奇数，f(a, b) = f(a, b/2);
如果 a 和 b 均为奇数，f(a, b) = f(b, a-b);
"""


class Solution:
    def gcd(self, a, b):
        if a < b:
            return self.gcd(b, a)
        if b == 0:
            return a
        aIsEven = a % 2 == 0
        bIsEven = b % 2 == 0
        if aIsEven and bIsEven:
            return 2 * self.gcd(a >> 1, b >> 1)
        elif aIsEven and not bIsEven:
            return self.gcd(a >> 1, b)
        elif not aIsEven and bIsEven:
            return self.gcd(a, b >> 1)
        else:
            return self.gcd(b, a - b)


if __name__ == '__main__':
    print(Solution().gcd(16, 12))
