"""
@Time    : 2020/8/23 20:16
@FileName: 08-23test02.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""


def test02():
    str1 = input().strip()
    arr = list(str1)
    k = int(input())
    res = []
    # temp = []
    for i in range(len(arr)):
        temp = ""
        for j in range(i, len(arr)):
            temp += arr[j]
            # if j != 0 and arr[j] == arr[j - 1]:
            #     continue
            if temp in res:
                continue
            res.append(temp)
            # temp += res[j]
    print(res)
    res.sort()
    print(res)
    print(res[k - 1])


if __name__ == '__main__':
    test02()
