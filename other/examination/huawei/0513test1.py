"""
@Time    : 2020/5/13 18:25
@FileName: 0513test1.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""

import datetime


def fun1():
    input1 = input().strip()
    # input1 = "1980 01 02 5|1980 01 04"
    # input1 = "1980 03 02 5|1980 04 03"
    input1 = input1.split("|")
    dictDay = {0: 7, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6}
    list1 = list(map(int, input1[0].split()))
    list2 = list(map(int, input1[1].split()))
    d1 = datetime.datetime(list1[0], list1[1], list1[2])
    d2 = datetime.datetime(list2[0], list2[1], list2[2])
    # print(str(d2 - d1).split(" ")[0])
    # listdiff = list(map(int, str(d2 - d1).split(" ")[0]))
    # print(listdiff)
    # print(d2 - d1)
    diffDay = int(str(d2 - d1).split(" ")[0])
    day = (diffDay + list1[-1]) % 7
    print(dictDay[day])


if __name__ == '__main__':
    fun1()
