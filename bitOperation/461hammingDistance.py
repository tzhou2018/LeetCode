'''
@Time    : 2020/3/12 22:16
@FileName: 461hammingDistance.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        z = x ^ y
        count = 0
        while z:
            if z & 1 == 1:
                count += 1
            z >>= 1
        return count
