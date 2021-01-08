"""
@Time    : 2020/8/23 20:02
@FileName: 08-23test01.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""


def test01():
    n, k = list(map(int, input().strip().split(" ")))
    arr = list(map(int, input().strip().split(" ")[:n]))
    arr.pop(k - 1)
    for e in arr:
        print(e, end=" ")


if __name__ == '__main__':
    test01()
