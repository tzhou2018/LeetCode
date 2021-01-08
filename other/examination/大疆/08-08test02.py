"""
@Time    : 2020/8/10 20:42
@FileName: 08-08test02.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""


class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        tmp = [[True] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if matrix[i * rows + j] == "#":
                    tmp[i][j] = False

        for i in range(rows):
            for j in range(cols):
                if self.find(matrix, rows, cols, i, j, path, tmp):
                    return True
        return False

    def find(self, matrix, rows, cols, i, j, path, tmp):
        if not path:
            return True
        index = i * cols + j
        if i < 0 or i >= rows or j < 0 or j >= cols \
                or matrix[index] != path[0] or not tmp[i][j]:
            return False
        tmp[i][j] = False
        if self.find(matrix, rows, cols, i + 1, j, path[1:], tmp) \
                or self.find(matrix, rows, cols, i - 1, j, path[1:], tmp) \
                or self.find(matrix, rows, cols, i, j - 1, path[1:], tmp) \
                or self.find(matrix, rows, cols, i, j + 1, path[1:], tmp):
            return True
        tmp[i][j] = True
        return False


if __name__ == '__main__':
    solution = Solution()
    n1 = int(input())
    alp = []
    max_cols = 0
    for i in range(n1):
        temp = input().strip()
        max_cols = max(max_cols, len(temp))
        alp.append(temp)
    for i in range(n1):
        nn = max_cols - len(alp[i])
        while nn > 0:
            alp[i] += "#"
            nn -= 1
    matrix = []
    for e in alp:
        matrix.extend(e)
    n2 = int(input().strip())
    res = []
    for i in range(n2):
        temp = input().strip()
        if solution.hasPath(matrix, n1, max_cols, temp):
            res.append(temp)
    res.sort()
    for e in res:
        print(e)
