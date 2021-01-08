"""
@Time       : 2020/9/9 21:43
@FileName   : 09_09test03.py
@Author     : Solarzhou
@Email      : t-zhou@foxmail.com
"""


def test0909():
    n = int(input().strip())
    arr = list(map(int, input().strip().split(" ")[:n]))

    while isDepulication(arr):
        de1 = de(arr)
        if not de1:
            break
        minV = de1[0]
        indexMin = arr.index(minV)
        arr.pop(indexMin)
        for i in range(len(arr)):
            if arr[i] == minV:
                arr[i] = 2 * minV
                break
    return arr


def de(arr):
    temp = {}
    tempd = {}
    for e in arr:
        temp[e] = temp.get(e, 0) + 1
    for k, v in temp.items():
        if v >= 2:
            tempd[k] = v
    return sorted(tempd)


def isDepulication(arr):
    temp = {}
    for e in arr:
        if e in temp:
            return True
        temp[e] = temp.get(e, 0) + 1
    return False


if __name__ == '__main__':
    res = test0909()
    for e in res:
        print(e, end=" ")
