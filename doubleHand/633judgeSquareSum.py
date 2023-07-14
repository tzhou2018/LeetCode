"""
@Time    : 2020/3/15 15:54
@FileName: 633judgeSquareSum.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""
import math


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if c < 0:
            return False
        left = 0
        right = int(math.sqrt(c))
        while left <= right:
            sqrtSum = left * left + right * right
            if sqrtSum == c:
                return True
            elif sqrtSum > c:
                right -= 1
            else:
                left += 1
        return False
