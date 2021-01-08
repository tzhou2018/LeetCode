"""
@Time       : 2020/9/11 20:42
@FileName   : 09_11test01.py
@Author     : Solarzhou
@Email      : t-zhou@foxmail.com
"""


def test01():
    n, m = list(map(int, input().strip().split(" ")))
    arr = []
    # res = [i for i in range(1, n + 1)]
    # return sorted(res)
    for i in range(m):
        temp = list(map(int, input().strip().split(" ")))
        arr.append(temp)
    if arr[0][-1] == 1 and arr[-1][-1] == 1:
        res = possible1(arr, n, m)
        return res
        pass
    elif arr[0][-1] == 0 and arr[-1][-1] == 0:
        res = possible2(arr, n, m)
        return res
    else:
        res = possible3(arr, n, m)
        return res


def possible1(arr, n, m):
    res = [arr[0][0]]
    temp = [i for i in range(1, n + 1)]
    for i in range(0, m):
        if arr[i][0] in temp:
            temp.remove(arr[i][0])
    res = res.extend(temp)
    return res


def possible2(arr, n, m):
    res = [arr[-1][0]]
    temp = [i for i in range(1, n + 1)]
    for i in range(0, m):
        if arr[i][0] in temp:
            temp.remove(arr[i][0])
    res = res.extend(temp)
    return res


def possible3(arr, n, m):
    res = []
    shang = []
    xia = []
    temp = [i for i in range(1, n + 1)]

    for e in arr:
        if e[1] == 1:
            shang.append(e[0])
        else:
            xia.append(e[0])
    allSX = shang + xia
    if len(shang) > len(xia):
        res.append(shang[0])
        shang.extend(xia)
        # res.append()
        for i in range(1, len(shang)):
            if shang[i] in temp:
                temp.remove(shang[i])
        return res.extend(temp)
    elif len(shang) < len(xia):
        res.append(xia[-1])
        # xia.extend(shang)
        shang.extend(xia)
        # res.append()
        for i in range(len(shang) - 1):
            if shang[i] in temp:
                temp.remove(shang[i])
        return res.extend(temp)
    else:
        x_temp = xia[-1]
        for e in shang:
            if e in xia:
                xia.remove(e)
        if not xia:
            res.append(shang[0])
            for i in range(len(shang)):
                if shang[i] in temp:
                    temp.remove(shang[i])
            # print(temp)
            res.extend(temp)
            # for e in temp:
            #     res.append(e)
            # print(res)
            return res
            # print(res.extend(temp))
            # res1 = res.append(temp)
            # return res1
        else:
            shang.extend(xia)
            for i in range(len(shang)):
                if shang[i] in temp:
                    temp.remove(shang[i])
            # print(temp)
            res.extend(temp)
            return res
            # print(res)
            # return res.extend(temp)

    # for e in xia:
    #     if e[0] in
    # temp = [i for i in range(1, n + 1)]


def possible4(arr):
    aa = [1, 1, 2]
    bb = [1]
    return bb.extend(aa)


if __name__ == '__main__':
    res = possible4("")
    print(res)
# res = test01()
# res.sort()
# for e in res:
#     print(e, end=" ")
# print(res)
# for e in res:
#     print(e, end=" ")
