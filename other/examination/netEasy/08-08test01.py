"""
@Time    : 2020/8/8 15:48
@FileName: 08-08test01.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""


def test1():
    n = int(input())
    arr = list(map(int, input().strip().split(" ")))[:n]
    res = 0
    for i in range(n):
        res += countPrime(arr[i])
    return res


def countPrime(n):
    if n < 2:
        return 0
    count = 0
    count = n //2
    # while n >= 2:
    #     n -= 2
    #     count += 1
    return count


if __name__ == '__main__':
    print(test1())
