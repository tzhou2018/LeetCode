'''
@Time    : 2020/3/4 16:09
@FileName: 242isAnagram.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str        :type t:
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
        for i in range(len(t)):
            count[ord(t[i]) - ord('a')] -= 1
        for i in range(26):
            if count[i] != 0:
                return False
        return True

    def fun(self, s, t):
        if len(s) != len(t):
            return False
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
        for i in range(len(t)):
            count[ord(t[i]) - ord('a')] -= 1
        for i in range(26):
            if count[i] != 0:
                return False
        return True
