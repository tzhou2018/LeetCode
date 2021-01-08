"""
@Time       : 2020/9/15 19:33
@FileName   : 09_15test02.py
@Author     : Solarzhou
@Email      : t-zhou@foxmail.com
"""


def test02():
    arr = input().strip()
    temp = []
    for e in arr:
        if e not in temp:
            temp.append(e)
    return temp


if __name__ == '__main__':
    res = test02()
    print("".join(res))
