"""
@Time    : 2020/8/22 20:16
@FileName: 08-22test02-yfd.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""


def test02(arr, rows, cols):
    dp = [[0] * cols for _ in range(rows)]
    dp[0][0] = arr[0][0]
    for i in range(1, cols):
        dp[0][i] = max(dp[0][i - 1], dp[0][i - 1] + arr[0][i])
    for j in range(1, rows):
        dp[j][0] = max(dp[j][0], dp[j - 1][0] + arr[j][0])
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = max(dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1],
                           dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + arr[i][j])
    res = 0
    for i in range(rows):
        res = max(res, dp[i])
    return res


if __name__ == '__main__':
    rows, cols = list(map(int, input().strip().split(" ")))
    arr = []
    for i in range(rows):
        arr.append(list(map(int, input().strip().split(" "))))
    res = test02(arr, rows, cols)
    print(res)
