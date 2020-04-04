'''
@Time    : 2020/3/17 14:07
@FileName: 278firstBadVersion.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
"""
如果第 m 个版本出错，则表示第一个错误的版本在 [l, m] 之间，
令 h = m；否则第一个错误的版本在 [m + 1, h] 之间，令 l = m + 1。

因为 h 的赋值表达式为 h = m，因此循环条件为 l < h。
"""
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while start < end:
            mid = start + (end - start) // 2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid + 1
        return start
