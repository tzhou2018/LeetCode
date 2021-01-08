"""
@Time       : 2020/9/13 20:39
@FileName   : 09_13test01.py
@Author     : Solarzhou
@Email      : t-zhou@foxmail.com
"""


def test02():
    n = int(input().strip())
    arr = list(map(int, input().strip().split(" ")))
    dp = getDp(arr)
    lenArr = len(arr)
    numC = {}
    maxV = max(dp)
    maxIndex = 0
    for i in range(lenArr - 1, -1, -1):
        if dp[i] == maxV:
            maxIndex = i
            break
    for i in range(maxIndex + 1):
        numC[dp[i]] = numC.get(dp[i], 0) + 1
    res = 1
    for k, v in numC.items():
        res *= v
    # print(numC)
    print(res % 1000000007)
# 9
# 2 1 5 3 6 4 8 9 9 10

def getDp(arr):
    lenArr = len(arr)
    dp = [1 for _ in range(lenArr)]
    for i in range(lenArr):
        dp[i] = 1
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    # print(dp)
    return dp


if __name__ == '__main__':
    # arr = [1, 3, 6, 4, 7]
    # getDp(arr)
    test02()
