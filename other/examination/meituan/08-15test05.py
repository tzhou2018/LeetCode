"""
@Time    : 2020/8/15 17:46
@FileName: 08-15test05.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""


def test05(n, m, arr):
    tempList = sorted(arr, key=lambda x: x[0])
    temp = [tempList[0][0], tempList[0][1]]
    count = 1
    res = [tempList[0][0]]
    for i in range(1, len(arr)):
        if tempList[i][0] not in temp:
            count += 1
        if tempList[i][0] not in res:
            res.append(tempList[i][0])
        temp.append(tempList[i][0])
    print(1)
    for e in res:
        print(e, end=" ")



if __name__ == '__main__':
    n, m = list(map(int, input().strip().split(" ")))
    arr = []
    for i in range(m):
        arr.append(list(map(int, input().strip().split(" "))))
    test05(n, m, arr)
