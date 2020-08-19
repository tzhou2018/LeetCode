"""
@Time    : 2020/8/11 10:14
@FileName: 0-1knapsackProblem.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""


def nkapsackProblem(vals, wts, n, w):
    if not vals or not wts:
        return 0
    dp = [[0] * (w + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, w + 1):
            if j - wts[i - 1] < 0:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - wts[i - 1]] + vals[i - 1])
    for i in range(n + 1):
        print(dp[i])
    # print(dp)
    return dp[n][w]


def nk(vals, wts, n, w):
    if not vals or not wts:
        return 0
    dp = [[0] * (w + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, w + 1):
            if j < wts[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - wts[i - 1]] + vals[i - 1])


if __name__ == '__main__':
    vals = [4, 2, 3]
    wts = [2, 1, 3]
    n = 3
    w = 4
    print(nkapsackProblem(vals, wts, n, 4))
