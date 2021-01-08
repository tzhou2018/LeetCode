"""
@Time    : 2020/8/23 21:24
@FileName: 08-23test05.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""


def test05():
    str1 = input().strip()
    n = int(input().strip())
    res = []
    queryList = []
    for i in range(n):
        queryList.append(list(map(int, input().strip().split(" "))))
    for e in queryList:
        count = 1
        # start, end = list(map(int, input().strip().split(" ")))
        start, end = e[0] - 1, e[1] - 1
        while start < end:
            if isSub(str1, start, end):
                break
            elif isSub(str1, start + 1, end):
                count += 1
                break
            elif isSub(str1, start, end - 1):
                count += 1
                break
            else:
                count += 2
                start += 1
                end -= 1
        res.append(count)
    for e in res:
        print(e)


def isSub(s, start, end):
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True


if __name__ == '__main__':
    test05()
