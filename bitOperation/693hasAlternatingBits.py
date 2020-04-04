'''
@Time    : 2020/3/14 14:16
@FileName: 693hasAlternatingBits.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


# 对于 1010 这种位级表示的数，把它向右移动 1 位得到 101，
# 这两个数每个位都不同，因此异或得到的结果为 1111。
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        res = n ^ (n >> 1)
        return res & (res + 1) == 0
