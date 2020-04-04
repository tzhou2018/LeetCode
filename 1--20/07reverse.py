'''
@Time    : 2020/2/9 21:09
@FileName: 07reverse.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ret = 0
        t = abs(x)
        while t:
            ret = 10 * ret + t % 10
            t //= 10
        if ret > 2 ** 32 or -ret < -2 ** 31:
            return 0
        return ret if x >= 0 else -ret


if __name__ == '__main__':
    print(Solution().reverse(1534236469))
