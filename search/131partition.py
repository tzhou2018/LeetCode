'''
@Time    : 2020/4/2 16:06
@FileName: 131partition.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


# 解法1
# 回溯
# 参考教程：https://leetcode-cn.com/problems/palindrome-partitioning/solution/hui-su-you-hua-jia-liao-dong-tai-gui-hua-by-liweiw/
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        sLen = len(s)
        res = []
        path = []
        self.backTracking(s, 0, sLen, path, res)
        return res

    def backTracking(self, s, start, sLen, path, res):
        # recursion terminate
        if start == sLen:
            res.append(path[:])
            return
            # precess logical in current level
        for i in range(start, sLen):
            if not self.isPalindrome(s, start, i):
                continue
            path.append(s[start:i + 1])
            self.backTracking(s, i + 1, sLen, path, res)
            path.pop()

    def isPalindrome(self, s, start, end):
        while start <= end:
            if s[start] != s[end]:
                return False
            else:
                start += 1
                end -= 1
        return True


# 方法2
# 优化上面解法，使用动态规划，以空间换取时间
class Solution1(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        sLen = len(s)
        res = []
        path = []
        dp = [[False] * sLen for _ in range(sLen)]
        for right in range(sLen):
            for left in range(right + 1):
                if s[left] == s[right] and (right - left <= 2 or dp[left + 1][right - 1]):
                    dp[left][right] = True
        self.backTracking(s, 0, sLen, path, res, dp)
        return res

    def backTracking(self, s, start, sLen, path, res, dp):
        # recursion terminate
        if start == sLen:
            res.append(path[:])
            return
            # precess logical in current level
        for i in range(start, sLen):
            if not dp[start][i]:
                continue
            path.append(s[start:i + 1])
            self.backTracking(s, i + 1, sLen, path, res, dp)
            path.pop()

if __name__ == '__main__':
    print(Solution1().partition("aab"))
