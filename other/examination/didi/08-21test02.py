"""
@Time    : 2020/8/21 20:13
@FileName: 08-21test02.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""


def test02(matrix, china, rows, cols):
    tmp = [True] * rows * cols
    count = 0
    for i in range(rows):
        for j in range(cols):
            res = find(matrix, tmp, rows, cols, i, j, china)
            count += res
    print(count // 4)


def find(matrix, tmp, rows, cols, i, j, path):
    count = 0
    if not path:
        return 1
    index = i * cols + j
    if i < 0 or i >= rows or j < 0 or j >= cols \
            or matrix[index] != path[0] or not tmp[index]:
        return 0
    tmp[index] = False
    # if find(matrix, tmp, rows, cols, i - 1, j, path[1:]) \
    #         or find(matrix, tmp, rows, cols, i + 1, j, path[1:]) \
    #         or find(matrix, tmp, rows, cols, i, j - 1, path[1:]) \
    #         or find(matrix, tmp, rows, cols, i, j + 1, path[1:]):
    #     return True
    count = find(matrix, tmp, rows, cols, i - 1, j, path[1:]) + \
            find(matrix, tmp, rows, cols, i + 1, j, path[1:]) + \
            find(matrix, tmp, rows, cols, i, j - 1, path[1:]) + \
            find(matrix, tmp, rows, cols, i, j + 1, path[1:])
    # if find(matrix, tmp, rows, cols, i - 1, j, path[1:]):
    #     count += 1
    # if find(matrix, tmp, rows, cols, i + 1, j, path[1:]):
    #     count += 1
    # if find(matrix, tmp, rows, cols, i, j - 1, path[1:]):
    #     count += 1
    # if find(matrix, tmp, rows, cols, i, j + 1, path[1:]):
    #     count += 1
    # return True
    tmp[index] = True
    return count


if __name__ == '__main__':
    n = int(input().strip())
    matrix = []
    for i in range(n):
        matrix.extend(input().strip())
    # matrix = list(matrix)
    test02(matrix, "CHINA", n, n)
