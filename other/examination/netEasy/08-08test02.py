"""
@Time    : 2020/8/8 16:13
@FileName: 08-08test02.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""


def test02():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split(" ")))[:n]
        arr.sort()
        index = len(arr) - 1
        people1 = arr[index]
        index -= 1
        people2 = arr[index]
        index -= 1
        less = index
        while index >= 0:
            if people1 == people2:
                less = min(less, index)
                people1 += arr[index]
                index -= 1
            if people1 > people2:
                people2 += arr[index]
                index -= 1
            elif people1 < people2:
                people1 += arr[index]
                index -= 1

        if people1 == people2:
            less = min(less, index)
        print(less + 1)


if __name__ == '__main__':
    test02()
