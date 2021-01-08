'''
@Time    : 2020/4/18 19:35
@FileName: outStock.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


def fun1():
    n, m = list(map(int, input().split()))
    arrStock = list(map(int, input().split()))[:n]
    arrStock.sort()
    Q = int(input())
    result = []
    for i in range(Q):
        q = int(input())
        if q <= m:
            # print(sum(arrStock[:q]))
            result.append(sum(arrStock[:q]))
        elif q > n:
            result.append(0)
        else:
            weightMul = 1
            res = 0
            days = (q + 1) // m
            tem = arrStock[:q]
            j = 0
            while days:
                res += sum(list(map(lambda a: a * weightMul, tem[(-m - j * m):(len(tem) - j * m)])))
                weightMul += 1
                days -= 1
                j += 1
            # print(res)
            result.append(res)
    for e in result:
        print(e)


if __name__ == '__main__':
    fun1()
