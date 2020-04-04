'''
@Time    : 2020/3/16 22:07
@FileName: 392isSubsequence.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''
"""
方法1：使用双指针
可以知道的是，当扫描s中的第k个字符时，假如它在t字符串中的第i位和第j位都出现过(i < j)，
那么我们从左到右扫描到第i位时，就认为已经找到了s中第k个字符。
因为i后面有更多的备选字符可以用来找s中的剩余字符。
也就是说，我们在t中找字符时，是严格不回溯的。这个问题可以使用双指针解决。

初始化指针i，j为0，分别指向s和j的第0个字符，在t中找到s[i]字符后，i++试图找下一个字符。

若最后i到达s末尾，则说明找到了该字符串
链接：https://leetcode-cn.com/problems/is-subsequence/solution/pan-duan-zi-xu-lie-shuang-zhi-zhen-fa-by-jarvis189/

# 方法2：find()函数，这种方法利用find的beg属性，动态规划起始位置
"""


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        i, j = 0, 0
        sLen = len(s)
        tLen = len(t)
        while i < sLen and j < tLen:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return True if i == sLen else False

    def isSubsequence1(self, s, t):
        if len(s) == 0:
            return True
        index = -1
        for e in s:
            index = t.find(e, index + 1)
            if index == -1:
                return False
        return True
