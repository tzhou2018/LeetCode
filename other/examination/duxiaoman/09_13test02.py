"""
@Time       : 2020/9/13 21:05
@FileName   : 09_13test02.py
@Author     : Solarzhou
@Email      : t-zhou@foxmail.com
"""


def test01():
    n, k = list(map(int, input().strip().split(" ")))
    matrix = [[] for _ in range(n)]
    # print(matrix)
    for i in range(n):
        temp = input().strip()
        for j in range(n):
            matrix[i].append(temp[j])
        # matrix.append([temp[0], temp[1], temp[2]])
    res = 0
    # res = find(matrix, n-1, n-1, 0, 0, k, res)
    print(k * k)


def find(matrix, rows, cols, i, j, k, res):
    index = i * cols + j
    if i < 0 or i >= rows or j < 0 or j >= cols:
        # res += 1
        return False
    if matrix[i][j] == "#":
        res += k
        res += 1
    elif matrix[i][j] == "1":
        res -= 1
    elif matrix[i][j] == "0":
        res += 1
    up = find(matrix, rows, cols, i + 1, j, k, res)
    left = find(matrix, rows, cols, i, j - 1, k, res)
    down = find(matrix, rows, cols, i + 1, j, k, res)
    right = find(matrix, rows, cols, i, j + 1, k, res)
    return min(up, down, left, right)


if __name__ == '__main__':
    test01()
