"""
@Time       : 2020/9/11 21:22
@FileName   : 09_11test02.py
@Author     : Solarzhou
@Email      : t-zhou@foxmail.com
"""


def test02():
    while True:
        str1 = input().strip()
        res = isNan(str1)
        print(res)


def isNan(str1):
    res = "Irregular password"
    daxie = False
    xiaoxie = False
    teshu = False
    shuzi = False
    if len(str1) < 8:
        return res
    for i in str1:
        # if xiaoxie or daxie or teshu or shuzi:
        #     continue
        if ord("z") >= ord(i) >= ord("a"):
            xiaoxie = True
        elif ord("Z") >= ord(i) >= ord("A"):
            daxie = True
        elif ord(str(9)) >= ord(i) >= ord(str(0)):
            shuzi = True
        else:
            teshu = True
    if daxie and xiaoxie and shuzi and teshu:
        return "Ok"
    else:
        return res


if __name__ == '__main__':
    test02()
