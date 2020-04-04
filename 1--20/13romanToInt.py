'''
@Time    : 2020/2/11 21:23
@FileName: 13romanToInt.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ans = 0
        for i in range(0, len(s) - 1):
            c = s[i]
            cAfter = s[i + 1]
            if d[c] < d[cAfter]:
                ans -= d[c]
            else:
                ans += d[c]
        ans += d[s[-1]]
        return ans
