"""
@Time    : 2020/8/6 19:37
@FileName: 08-06test01.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""
"""
题目描述：
X星人的基因由A、B、C、D、E五种不同的结构组合而成。

如果两个性别不同的X星人的基因序列相似度大于50%，按照X星的法律他们是禁止结婚的，等于50%据说还是可以的。

那么基因的相似度怎么计算呢？分别从两个人身上取长度均为N的基因片段，如果它们的最长公共子序列
（注意，最长公共子序列不需要连续）的长度为M，则相似度=M/N。是不是很简单呢？

现在给你两段X星人的基因序列片段，请你判断他们是不是可以结婚？
"""

def test():
    n = int(input())
    arr1 = input().strip().split(" ")
    arr2 = input().strip().split(" ")
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = 1 if arr2[0] == arr1[0] else 0
    for i in range(1, n):
        dp[0][i] = max(dp[0][i - 1], 1 if arr1[0] == arr2[i] else 0)
    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][0], 1 if arr2[0] == arr1[i] else 0)
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            if arr1[i] == arr2[j]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
    res = dp[-1][-1] / n
    return round(res, 2)


if __name__ == '__main__':
    res = test()
    if res <= 0.5:
        yes = " Yes "
        print(res, end="")
        print(yes, end="")
    else:
        print(res, end="")
        print(" No ")
