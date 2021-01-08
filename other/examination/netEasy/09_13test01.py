"""
@Time       : 2020/9/13 11:09
@FileName   : 09_13test01.py
@Author     : Solarzhou
@Email      : t-zhou@foxmail.com
"""


def test01():
    str1 = input().strip()
    mo = ["0", "1", "10", "11", "100", "101", "110", "111"]
    count = [0]

    def isMo(res, index, str2):
        global sLen
        if res == str1:
            count[0] += 1
            return
        for i in range(index, len(str1) - 1):
            if str2[0:i + 1] in mo:
                res += str1[0:i + 1]
                str2 = str1[i + 1:]
                isMo(res, index + i, str2)
            # if str1[i:] in mo:
            #     sLen = len(str1) - i
            #     res += str1[i:]
            #
            # elif str1[i] in mo:
            #     sLen = i
            #     res += str1[i]
            # else:
            #     sLen = i
            #
            #     continue
            # isMo(res, sLen + 1)

    isMo("", 0, str1[:])
    print(count[0] + 1)


def test01_1():
    str1 = input().strip()
    mo = ["0", "1", "10", "11", "100", "101", "110", "111"]
    count = [0]
    for i in range(len(str1)):
        if str1[0:i + 1] in mo:
            pass
    pass


def test01_3():
    str1 = input().strip()
    print(len(str1))


if __name__ == '__main__':
    test01_3()
