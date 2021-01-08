"""
@Time    : 2020/8/15 16:42
@FileName: 08-15test02.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""


def test02(n, arr):
    start = arr[0]
    count = 0
    index = 1
    arrLen = len(arr)
    while index < arrLen:
        if arr[index] == start:
            count += 1
            if index + 1 < arrLen:
                # index += 1
                start = arr[index + 1]
            # else:
        index += 2
    print(count)


if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for i in range(n):
        arr.extend(input().strip().split(" "))
    test02(n, arr)
