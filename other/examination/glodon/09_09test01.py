"""
@Time       : 2020/9/9 20:43
@FileName   : 09_09test01.py
@Author     : Solarzhou
@Email      : t-zhou@foxmail.com
"""


def test01():
    n, m, x = list(map(int, input().strip().split(" ")))
    arr = list(map(int, input().strip().split(" ")))
    minV = min(arr)
    indexMin = arr.index(minV)
    print(minV, indexMin)
    index = indexMin
    for i in range(m):
        arr[indexMin] += x
        minV = min(arr)
        indexMin = arr.index(minV)
    print(arr[index])


if __name__ == '__main__':
    test01()
