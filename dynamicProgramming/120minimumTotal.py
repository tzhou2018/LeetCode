'''
@Time    : 2020/2/14 20:36
@FileName: 120minimumTotal.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


# 动态规划，从上往下分析，从下网上计算
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        rows = len(triangle)
        res = [[0 for _ in range(rows)] for _ in range(rows)]
        res[rows - 1] = triangle[rows - 1][:]
        for i in range(rows - 2, -1, -1):
            row = triangle[i][:]
            for j in range(i + 1):
                res[i][j] = min(res[i + 1][j], res[i + 1][j + 1]) + row[j]
        return res[0][0]


if __name__ == '__main__':
    print(Solution().minimumTotal([
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]))
    # print(Solution().minimus())
