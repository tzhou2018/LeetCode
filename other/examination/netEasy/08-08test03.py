"""
@Time    : 2020/8/8 15:19
@FileName: 08-08test03.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""


def test3():
    n = int(input())
    arr = list(map(int, input().strip().split(" ")))
    # n = 1
    # arr = [5]
    arr.sort(reverse=True)
    count = 0
    res = sum(arr)
    tem = res
    while tem > 0:
        if tem % 10 == 5:
            lastPop = arr.pop()
            count += lastPop
            if arr:
                res = sum(arr) + count - lastPop
                tem = res
                continue
            else:
                return 0
        tem = tem // 10
    return res


if __name__ == '__main__':
    res = test3()
    print(res)
