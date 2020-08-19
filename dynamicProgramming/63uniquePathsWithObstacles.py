'''
@Time    : 2020/2/15 10:51
@FileName: 63uniquePathsWithObstacles.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
            return 0
        if obstacleGrid[0][0] == 1:
            return 0
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        res = [[0] * cols for _ in range(rows)]
        res[0][0] = 1
        for i in range(1, rows):
            res[i][0] = 0 if obstacleGrid[i][0] == 1 else res[i - 1][0]
        for i in range(1, cols):
            res[0][i] = 0 if obstacleGrid[0][i] == 1 else res[0][i - 1]
        for i in range(1, rows):
            for j in range(1, cols):
                res[i][j] = 0 if obstacleGrid[i][j] == 1 else \
                    (res[i - 1][j] + res[i][j - 1])
        # return res[-1][-1]
        return res[rows - 1][cols - 1]


if __name__ == '__main__':
    print(Solution().uniquePathsWithObstacles([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]))
