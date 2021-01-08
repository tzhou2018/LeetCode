"""
@Time       : 2020/9/12 19:25
@FileName   : 09_12test01.py
@Author     : Solarzhou
@Email      : t-zhou@foxmail.com
"""


def test01():
    n, m = list(map(int, input().strip().split(" ")))
    arr = list(map(int, input().strip().split(" ")[:n]))
    preHalf = arr[:n // 2]
    nextHalf = arr[n // 2:]
    res = []
    for i in range(m):
        res.clear()
        while nextHalf or preHalf:
            if nextHalf:
                res.append(nextHalf.pop(0))
            if preHalf:
                res.append(preHalf.pop(0))
        preHalf = res[:n // 2]
        nextHalf = res[n // 2:]
    for e in res:
        print(e, end=" ")
    # print(res)


if __name__ == '__main__':
    test01()
