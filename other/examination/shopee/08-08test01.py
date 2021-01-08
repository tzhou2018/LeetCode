"""
@Time    : 2020/8/8 20:43
@FileName: 08-08test01.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""


def test01():
    str1 = input().strip()
    # str1 = "CapitalizedWords"
    res = ""
    str1 = list(str1)
    for i in range(len(str1)):
        if not isA_Z(str(str1[i])):
            continue
        if not res:

            res += str1[i].lower()
        elif not isA_Z(str(str1[i - 1])):
            res += str1[i].upper()
        elif isA_Z(str1[i]):
            res += str1[i].lower()
    return res


def isA_Z(s):
    if ord("0") <= ord(s) <= ord("9") \
            or ord("a") <= ord(s) <= ord("z") \
            or ord("A") <= ord(s) <= ord("Z"):
        return True
    else:
        return False


if __name__ == '__main__':
    res = test01()
    print(res)
