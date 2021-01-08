"""
@Time    : 2020/8/15 17:14
@FileName: 08-15-test04.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""


def test03(m, a, b, arr):


    temp2 = sorted(arr, key=lambda x: x[0], reverse=False)
    res2 = 0
    for _ in range(a):
        if temp2[-1][0] - temp2[1] >= 0:
            res2 += temp2.pop()[0]
    temp2 = sorted(temp2, key=lambda x: x[1], reverse=False)
    for _ in range(b):
        res2 += temp2.pop()[1]


    temp2 = sorted(arr, key=lambda x: x[1], reverse=False)
    res3 = 0
    for _ in range(b):
        res3 += temp2.pop()[1]
    temp2 = sorted(temp2, key=lambda x: x[0], reverse=False)
    for _ in range(a):
        if temp2[-1][0] - temp2[1] >= 0:
            res3 += temp2.pop()[0]

    print(max(res2, res3))


if __name__ == '__main__':
    n, a, b = list(map(int, input().strip().split(" ")))
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().strip().split(" "))))
    test03(n, a, b, arr)
