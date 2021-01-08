"""
@Time    : 2020/8/15 17:14
@FileName: 08-15-test04.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""


def test03(m, a, b, arr):
    temp = sorted(arr, key=lambda x: x[0] - x[1], reverse=False)
    # print(temp)
    res1 = 0
    for _ in range(a):
        res1 += temp.pop()[0]
    temp = sorted(temp, key=lambda x: x[1] - x[0], reverse=False)
    # print(temp)
    for _ in range(b):
        res1 += temp.pop()[1]

    temp2 = sorted(arr, key=lambda x: x[0], reverse=False)
    res2 = 0
    for _ in range(a):
        res2 += temp2.pop()[0]
    temp2 = sorted(temp2, key=lambda x: x[1], reverse=False)
    for _ in range(b):
        res2 += temp2.pop()[1]
    print(max(res1, res2))


if __name__ == '__main__':
    n, a, b = list(map(int, input().strip().split(" ")))
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().strip().split(" "))))
    test03(n, a, b, arr)
