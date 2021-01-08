"""
@Time       : 2020/9/12 19:44
@FileName   : 09_12test03.py
@Author     : Solarzhou
@Email      : t-zhou@foxmail.com
"""


def test03():
    t = int(input())
    resList = []
    for i in range(t):
        arr = input().strip().split(" ")
        k = int(arr[-1])
        str1 = arr[0]
        str2 = arr[1]
        str3 = arr[2]
        n = 0
        str3Len = len(str3)
        str1Len = len(str1)
        str2Len = len(str2)
        start = 0
        start1 = 0
        start2 = 0
        res = ""
        count = 0
        flag = True
        if not str1 or not str2 or not str3:
            # print(0)
            resList.append(0)
            return
        while start < str3Len and (start1 < len(str1) or start2 < len(str2)):
            startT1 = start
            temp1 = start1
            while start1 < str1Len and startT1 < str3Len:
                if str1[start1] == str3[startT1]:
                    start1 += 1
                    startT1 += 1
                else:
                    break

            startT2 = start
            temp2 = start2
            while start2 < str2Len and startT2 < str3Len:
                if str2[start2] == str3[startT2]:
                    start2 += 1
                    startT2 += 1
                else:
                    break
            maxLen = max(start1, start2)

            if maxLen == start1 and start1 != temp1:
                start2 = temp2
                res += str1[temp1:start1]
                count += 1
                start = startT1
                # str1 = str1[]
            elif maxLen == start2 and start2 != temp2:
                start1 = temp1
                res += str2[temp2:start2]
                count += 1
                start = startT2
            # print(res, count)
            if start1 == temp1 and start2 == temp2:
                flag = not flag
                break
        if flag:
            if res == str3 and count <= k:
                # print(1)
                resList.append(1)
            else:
                # print(0)
                resList.append(0)
        else:
            # print(0)
            resList.append(0)
    for e in resList:
        print(e)


if __name__ == '__main__':
    test03()
