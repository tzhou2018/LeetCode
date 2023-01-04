"""
@Time    : 2020/3/4 21:45
@FileName: 205isIsomorphic.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))


class Solution2:
    def isIsomorphic(self, s, t):
        s2t = {}
        t2s = {}
        if len(s) != len(t):
            return False
        lenS = len(s)
        for i in range(lenS):
            x = s[i]
            y = t[i]
            if (s2t.__contains__(x) and s2t[x] != y) \
                    or (t2s.__contains__(y) and t2s[y] != x):
                return False
            s2t[x] = y
            t2s[y] = x
        return True
