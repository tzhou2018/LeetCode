"""
@Time       : 2020/9/13 15:33
@FileName   : 09_13test02.py
@Author     : Solarzhou
@Email      : t-zhou@foxmail.com
"""


def test02():
    arr = list(map(int, input().strip().split(" ")))
    times = 0
    res = 0
    for e in arr:
        # if e == pre:
        if times == 0:
            res = e
            times += 1
        elif res == e:
            times += 1
        else:
            times -= 1
    return res if arr.count(res) * 2 > len(arr) else 0


if __name__ == '__main__':
    res = test02()
    print(res)
