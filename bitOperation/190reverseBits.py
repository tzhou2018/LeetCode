'''
@Time    : 2020/3/13 21:35
@FileName: 190reverseBits.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution:
    # @param n, an integer
    # @return an integer
    # res 依次左移，n 依次右移
    def reverseBits(self, n):
        res = 0
        mark = 1
        for _ in range(32):
            res <<= 1
            if n & mark:
                res |= 1
            n >>= 1
        return res
