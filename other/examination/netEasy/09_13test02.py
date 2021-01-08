"""
@Time       : 2020/9/13 10:49
@FileName   : 09_13test02.py
@Author     : Solarzhou
@Email      : t-zhou@foxmail.com
"""


def test02():
    arr = list(map(int, input().strip().split(" ")))
    lenArr = len(arr)
    maxLen = 0
    for i in range(lenArr-1):
        maxV = arr[i]
        minV = arr[i]
        for j in range(i+1, lenArr):
            maxV = max(maxV, arr[j])
            minV = min(minV, arr[j])
            if maxV - minV == 1:
                maxLen = max(maxLen, j - i + 1)
            elif maxV == minV:
                continue
            else:
                break
    print(maxLen)


if __name__ == '__main__':
    test02()
