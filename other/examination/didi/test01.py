"""
@Time    : 2020/8/21 19:26
@FileName: test01.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""


def addValue(matrix, fibList, tr, tc, dr, dc):
    if tr == dr:
        for i in range(tc, dc + 1):
            matrix[tc][i] = fibList.pop()
    elif tc == dc:
        for i in range(tr, dr + 1):
            matrix[i][tc] = fibList.pop()
    else:
        curC = tc
        curR = tr
        while curC != dc:
            matrix[tc][curC] = fibList.pop()
            curC += 1
        while curR != dr:
            matrix[curR][dc] = fibList.pop()
            curR += 1
        while curC != tc:
            matrix[dr][curC] = fibList.pop()
            curC -= 1
        while curR != tr:
            matrix[curR][tc] = fibList.pop()
            curR -= 1


def test01(n):
    if n < 2:
        print(n)
        return
    item1, item2 = 0, 1
    fibonacciList = [1]
    for _ in range(2, n * n + 1):
        ans = item1 + item2
        item1, item2 = item2, ans
        fibonacciList.append(ans)
    res = [[0] * n for _ in range(n)]
    tr, tc = 0, 0
    dr, dc = n - 1, n - 1
    while tr <= dr and tc <= dc:
        addValue(res, fibonacciList, tr, tc, dr, dc)
        tr += 1
        tc += 1
        dr -= 1
        dc -= 1
    for i in range(n):
        for j in range(n):
            print(res[i][j], end=" ")
        print()


if __name__ == '__main__':
    n = int(input())
    test01(n)
