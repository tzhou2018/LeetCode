'''
@Time    : 2020/3/16 15:42
@FileName: 455findContentChildren.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''

"""
给一个孩子的饼干应当尽量小并且又能满足该孩子，这样大饼干才能拿来给满足度比较大的孩子。
因为满足度最小的孩子最容易得到满足，所以先满足满足度最小的孩子。
"""
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        gLen = len(g) -1
        sLen = len(s) -1
        gi, si = 0, 0
        while gi <= gLen and si <= sLen:
            if s[si] >= g[gi]:
                gi += 1
            si += 1
        return gi
