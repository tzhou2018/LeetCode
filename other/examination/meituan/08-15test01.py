"""
@Time    : 2020/8/15 16:05
@FileName: 08-15test01.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""


def test02(m):
    count = 0
    res = []
    n = m
    while n > 1:
        reverN = reverseN(n)
        temp = n * 4
        if reverN == temp and temp <= m:
            count += 1
            res.append((n, temp))
        n -= 1
    res = sorted(res, key=lambda x: x[0])
    if count == 0:
        print(0)
    else:
        print(count)
        for e in res:
            print(e[0], end=" ")
            print(e[1])


def reverseN(n):
    res = ""
    while n > 0:
        res += str(n % 10)
        n = n // 10
    return int(res)


if __name__ == '__main__':
    # print(test01(10000))
    # n = int(input().strip())
    # test01(n)
    print("hello")
