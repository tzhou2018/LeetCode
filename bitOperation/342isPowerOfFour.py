'''
@Time    : 2020/3/14 14:09
@FileName: 342isPowerOfFour.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num & (num - 1) == 0 and (num - 1) % 3 == 0
