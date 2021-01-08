"""
@Time       : 2020/9/12 13:52
@FileName   : 09_12test01.py
@Author     : Solarzhou
@Email      : t-zhou@foxmail.com
"""


def test01():
    arr = list(map(int, input().strip().split(",")))
    left = 0
    right = len(arr) - 1
    while left < right:
        while left < right and arr[left] & 1 != 0:
            left += 1
        while left < right and arr[right] & 1 == 0:
            right -= 1
        swap(arr, left, right)
        left += 1
        right -= 1
    return arr


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
    res = test01()
    print(res)
