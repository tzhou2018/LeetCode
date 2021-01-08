"""
@Time       : 2020/9/13 15:26
@FileName   : 09_13test01.py
@Author     : Solarzhou
@Email      : t-zhou@foxmail.com
"""


def test01():
    str1 = input().strip()
    lenStr = len(str1)
    if lenStr < 2:
        return lenStr
    dp = [1 for _ in range(lenStr)]
    mapD = {}
    mapD[str1[0]] = 0
    for i in range(1, lenStr):
        if str1[i] in mapD:
            if i - mapD[str1[i]] > dp[i - 1]:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = i - mapD[str1[i]]
        else:
            dp[i] = dp[i - 1] + 1
        mapD[str1[i]] = i
    return max(dp)


if __name__ == '__main__':
    res = test01()
    print(res)
