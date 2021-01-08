"""
@Time    : 2020/8/23 20:40
@FileName: 08-22test03.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""


def numberAdd(n):
    sumN = 0
    while n > 0:
        sumN += n % 10
        n //= 10
    return sumN


def test03(t):
    res = []
    for i in range(t):
        number = int(input())
        # secondAdd = numberAdd(number // 2) + numberAdd(number // 2)
        maxAdd = 0
        start = 0
        end = number
        while start <= end:
            temp = start + end
            if temp == number:
                maxAdd = max(maxAdd, numberAdd(end) + numberAdd(start))
                if maxAdd > number // 2:
                    break
                start += 1
                end -= 1
            elif temp < number:
                start += 1
            else:
                end -= 1
        res.append(maxAdd)
    for e in res:
        print(e)
    # return res


if __name__ == '__main__':
    t = int(input())
    test03(t)
    # print(test03(t))
