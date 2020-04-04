'''
@Time    : 2020/3/5 10:11
@FileName: 696countBinarySubstrings.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''

# 遍历所给字符串，记录当前数字相同的连续子串长度为 curLen，
# 与相邻的不同子串长度 preLen 做比较。
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        preLen, curLen, count = 0, 1, 0
        sLen = len(s)
        for i in range(1, sLen):
            if s[i] == s[i - 1]:
                curLen += 1
            else:
                preLen = curLen
                curLen = 1
            if preLen >= curLen:
                count += 1
        return count
