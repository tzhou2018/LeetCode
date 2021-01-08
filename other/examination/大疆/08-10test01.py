"""
@Time    : 2020/8/10 19:34
@FileName: 08-10test01.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""


# 喝咖啡解题
def test01():
    n = int(input().strip())
    a = int(input().strip())
    x = int(input().strip())
    nBug = []
    res = 0
    for _ in range(n):
        nBug.append(int(input().strip().strip()))
    allMin = sum(nBug)
    temp = allMin // a
    if allMin / a <= x * 60:
        if allMin / a > temp:
            return temp + 1
        else:
            return temp
    else:
        time1 = allMin - a * 60 * x
        time2 = time1 + a * 60
        if time2 > 480:
            return 0
        else:
            return time2
    # for i in range(n):
    #     temp = nBug[i] // a
    #     if x > 0:
    #         if nBug[i] / a > temp:
    #             res += temp + 1
    #         else:
    #             res += temp
    #         x -= 1
    #     else:
    #         res += nBug[i]
    # return 0 if res > 480 else res


if __name__ == '__main__':
    print(test01())
