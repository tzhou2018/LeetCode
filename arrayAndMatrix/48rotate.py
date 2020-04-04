'''
@Time    : 2020/2/17 15:00
@FileName: 48rotate.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''

# 思路：
# 首先将原数组 第一列 与 最后一列互换，第二列与倒数第二列互换 ......
# 之后将相应对角元素互换

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return
        h = len(matrix)
        w = len(matrix[0])
        for i in range(0, h):
            for j in range(0, w // 2):
                matrix[i][j], matrix[i][w - j - 1] = matrix[i][w - j - 1], matrix[i][j]

        for i in range(0, h):
            for j in range(0, w - 1 - i):
                matrix[i][j], matrix[w - 1 - j][h - 1 - i] = matrix[w - 1 - j][h - 1 - i], matrix[i][j]
