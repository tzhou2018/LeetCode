'''
@Time    : 2020/3/14 13:46
@FileName: 231isPowerOfTwo.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and n & (n - 1) == 0

    # 思路2
    # 一个数与它的相反数作与运算，若是结果等于这个树，则满足条件
    def isPowerOfTwo2(self, n):
        return n != 0 and n & -n == n
