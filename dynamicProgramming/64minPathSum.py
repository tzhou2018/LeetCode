'''
@Time    : 2020/2/15 11:37
@FileName: 64minPathSum.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        res = [[0] * cols for _ in range(rows)]
        res[0][0] = grid[0][0]
        for i in range(1, cols):
            res[0][i] = grid[0][i] + res[0][i - 1]
        for i in range(1, rows):
            res[i][0] = res[i - 1][0] + grid[i][0]
        for i in range(1, rows):
            for j in range(1, cols):
                res[i][j] = min(res[i - 1][j], res[i][j - 1]) + grid[i][j]
        return res[-1][-1]


if __name__ == '__main__':
    print(Solution().minPathSum([
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]))
