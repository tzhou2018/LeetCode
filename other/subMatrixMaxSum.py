'''
@Time    : 2020/4/3 15:22
@FileName: subMatrixMaxSum.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


def subMatrixMaxSum(m):
    rows = len(m)
    cols = len(m[0])
    Max = float('-inf')
    for i in range(rows):
        tem = [0] * cols
        for j in range(i, rows):
            cur = 0
            for k in range(0, cols):
                tem[k] += m[i][k]
                cur += tem[k]
                Max = max(Max, cur)
                cur = 0 if cur < 0 else cur
    return Max


if __name__ == '__main__':
    matrix = [[1, -2, 3],
              [-1, 2, -3],
              [2, 34, 5]]
    matrix1 = [[1, -3, 3]]
    print(subMatrixMaxSum(matrix))
