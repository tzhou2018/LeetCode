'''
@Time    : 2020/2/15 10:16
@FileName: 60uniquePaths.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = [[1 for i in range(m)] for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                res[i][j] = res[i - 1][j] + res[i][j - 1]
        return res[n - 1][-1]


if __name__ == '__main__':
    print(Solution().uniquePaths(7, 3))
