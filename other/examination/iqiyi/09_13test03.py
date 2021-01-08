"""
@Time       : 2020/9/13 15:43
@FileName   : 09_13test03.py
@Author     : Solarzhou
@Email      : t-zhou@foxmail.com
"""


def test03():
    arr = list(map(int, input().strip().split(" ")))
    res = []
    arr.sort()
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        target = 0 - arr[i]
        start = i + 1
        end = len(arr) - 1
        while start < end:
            if arr[start] + arr[end] > target:
                end -= 1
            elif arr[start] + arr[end] < target:
                start += 1
            else:
                res.append((arr[i], arr[start], arr[end]))
                end -= 1
                start += 1
                while start < end and arr[start] == arr[start - 1]:
                    start += 1
                while start < end and arr[end] == arr[end + 1]:
                    end -= 1
    return res


if __name__ == '__main__':
    res = test03()
    for e in res:
        print("%d %d %d" % (e[0], e[1], e[2]))
        # print(e[0], e[1])
