"""
@Time       : 2020/9/13 10:18
@FileName   : 09_13test05.py
@Author     : Solarzhou
@Email      : t-zhou@foxmail.com
"""


def test05():
    x = int(input())
    arr = list(map(int, input().strip().split(" ")))
    arr.sort()
    count = 0
    arrLen = len(arr)
    while arr:
        if len(arr) > 1 and arr[0] + arr[-1] <= x:
            count += 1
            arr.pop(0)
            arr.pop()
        elif arr[-1] <= x:
            count += 1
            arr.pop()
        elif arr[0] > x:
            arr.pop(0)
            continue
        else:
            count += 1
            arr.pop(0)
    print(count)


if __name__ == '__main__':
    test05()
