'''
@Time    : 2020/2/28 20:07
@FileName: test2.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


def fun1():
    n = int(input())
    play1 = input()
    play2 = input()
    play1 = list(map(int, play1.split()))
    play2 = list(map(int, play2.split()))
    play1.sort(reverse=True)
    play2.sort(reverse=True)
    res1 = 0
    res2 = 0
    for i in range(3):
        res1 += play1[i]
        res2 += play2[i]
    return max(res1, res2)


if __name__ == '__main__':
    print(fun1())
