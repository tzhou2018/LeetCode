"""
@Time       : 2020/9/5 15:24
@FileName   : 09_05test01.py
@Author     : Solarzhou
@Email      : t-zhou@foxmail.com
"""


def test01(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    # if n == 2:
    #     return 1
    res = 0
    n1, n2 = 0, 1
    for i in range(2, n + 1):
        res = n1 + n2
        n1, n2 = n2, res
    return res


if __name__ == '__main__':
    n = int(input())
    res = test01(n)
    print(res)
