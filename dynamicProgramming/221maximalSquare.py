'''
@Time    : 2020/2/15 14:24
@FileName: 221maximalSquare.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        if len(matrix[0]) == 0:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        res = [[0] * cols for _ in range(rows)]
        maxSide = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        res[i][j] = 1
                    else:
                        res[i][j] = min(res[i][j - 1], res[i - 1][j], res[i - 1][j - 1]) + 1
                maxSide = max(maxSide, res[i][j])
        return maxSide * maxSide

if __name__ == '__main__':
    # print(Solution().maximalSquare([[1, 0, 1, 0, 0],
    #                                 [1, 0, 1, 1, 1],
    #                                 [1, 1, 1, 1, 1],
    #                                 [1, 0, 0, 1, 0]]))
    print(Solution().maximalSquare(
        [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))
    print(Solution().maximalSquare([['1']]))
