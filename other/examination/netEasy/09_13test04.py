"""
@Time       : 2020/9/13 11:48
@FileName   : 09_13test04.py
@Author     : Solarzhou
@Email      : t-zhou@foxmail.com
"""


def test04():
    n, k, m = list(map(int, input().strip().split(" ")))
    arr = []
    for i in range(m):
        arr.append(list(map(int, input().strip().split(" "))))
    print(m)


if __name__ == '__main__':
    test04()
