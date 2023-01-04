"""
@Time    : 2020/3/4 21:12
@FileName: 409longestPalindrome.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        palindrome = 0
        sDict = {}
        for i in s:
            sDict[i] = sDict.get(i, 0) + 1
        for key in sDict:
            palindrome += sDict[key] // 2 * 2
        if palindrome < len(s):
            palindrome += 1
        return palindrome