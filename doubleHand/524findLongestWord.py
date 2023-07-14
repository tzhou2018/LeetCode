"""
@Time    : 2020/3/15 21:15
@FileName: 524findLongestWord.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""


# 思路：
# 遍历所给字符串字典，依次判断所给字符串字典中的字符串是否是 s 的子串，
# 取最长的字符串
class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        longestString = ''
        for e in d:
            l1 = len(longestString)
            l2 = len(e)
            if l1 > l2 or (l1 == l2 and longestString < e):
                continue
            isSubString = self.isSubstring(s, e)
            if isSubString:
                longestString = e
        return longestString

    def isSubstring(self, s, target):
        i, j = 0, 0
        while i < len(s) and j < len(target):
            if s[i] == target[j]:
                j += 1
            i += 1
        return j == len(target)
