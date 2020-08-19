'''
@Time    : 2020/3/4 22:18
@FileName: 647countSubstrings.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''
"""
从字符串的某一位开始，尝试着去扩展子字符串。
"""


class Solution(object):
    count = 0

    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        sLen = len(s)
        for i in range(sLen):
            self.extendSubstrings(s, i, i)  # 奇数长度
            self.extendSubstrings(s, i, i + 1)  # 偶数长度
        return self.count

    def extendSubstrings(self, s, start, end):
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
            self.count += 1

if __name__ == '__main__':
    print(Solution().countSubstrings("aba"))
