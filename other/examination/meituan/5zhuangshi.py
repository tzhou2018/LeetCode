"""
@Time    : 2020/8/15 19:31
@FileName: 5zhuangshi.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""


def test05(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, m + 1):
        dp[1][i] = m // i
    for i in range(2, n + 1):
        for j in range(1, m + 1):
            for k in range(j, m + 1, j):
                dp[i][j] = dp[i][j] + dp[i - 1][k]
    for i in range(n + 1):
        print(dp[i])


if __name__ == '__main__':
    test05(2, 4)
