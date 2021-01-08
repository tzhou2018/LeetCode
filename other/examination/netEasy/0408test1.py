'''
@Time    : 2020/4/25 10:10
@FileName: 0408test1.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''

"""
作者：胡萬三
链接：https://www.nowcoder.com/discuss/402598
来源：牛客网

英雄与怪兽。更新二维数组中的值
n*m的地图上，每个位置值为0或1，0表示怪兽，1表示英雄，对于每个英雄求出离他最近的怪兽的距离是多少，
矩阵中每个位置离上下左右的距离都是1，若当前位置是怪兽，输出0即可，题目保证至少存在一只怪兽
输出更新后的矩阵
"""
class Solution:
    def has(self, matrix, rows, cols):
        # write code here
        tmp = [[0] * cols for i in range(rows)]
        res = [[0] * cols for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    pathSum = self.find(matrix, rows, cols, i, j, tmp)
                    res[i][j] = pathSum
                else:
                    continue
        return res

    def find(self, matrix, rows, cols, i, j, tmp):
        if i < 0 or i >= rows or j < 0 or j >= cols or tmp[i][j] == 1:
            # if i < 0 or i >= rows or j <0 or j >= cols
            return 1
        if matrix[i][j] == 0:
            return 0
        tmp[i][j] = 1
        c1 = 1 + self.find(matrix, rows, cols, i + 1, j, tmp)
        c2 = 1 + self.find(matrix, rows, cols, i - 1, j, tmp)
        c3 = 1 + self.find(matrix, rows, cols, i, j - 1, tmp)
        c4 = 1 + self.find(matrix, rows, cols, i, j + 1, tmp)
        tmp[i][j] = 0

        return min(c1, c2, c3, c4)


if __name__ == '__main__':
    # matrix = [[1, 1, 1], [0, 1, 0], [1, 0, 1]]
    # rows = len(matrix)
    # cols = len(matrix[0])
    rows = int(input())
    cols = rows
    matrix = []
    for _ in range(rows):
        matrix.append(list(map(int, input().split())))

    print(Solution().has(matrix, rows, cols))
