"""
@Time       : 2020/9/10 19:36
@FileName   : 09_10test01.py
@Author     : Solarzhou
@Email      : t-zhou@foxmail.com
"""


def test02():
    arr = input().strip()
    if not arr:
        return 0
    arr = list(map(int, arr.split(" ")))
    lenNums = len(arr)
    # if lenNums == 0:
    #     return 0
    dp = [1 for _ in range(lenNums)]
    maxSub = 1
    for i in range(lenNums):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[j] + 1, dp[i])
        maxSub = max(maxSub, dp[i])
    # print(maxSub)
    return maxSub


if __name__ == '__main__':
    res = test02()
    print(res)
