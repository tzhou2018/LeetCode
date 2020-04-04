'''
@Time    : 2020/3/9 20:36
@FileName: 766isToeplitzMatrix.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            if not self.check(matrix, matrix[i][0], i, 0):
                return False
        for i in range(cols):
            if not self.check(matrix, matrix[0][i], 0, i):
                return False
        return True

    def check(self, matrix, value, row, col):
        if row >= len(matrix) or col >= len(matrix[0]):
            return True
        if matrix[row][col] != value:
            return False
        return self.check(matrix, value, row + 1, col + 1)
