'''
@Time    : 2020/4/18 20:31
@FileName: jumpGezi.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


def fun1():
    n, h0 = list(map(int, input().split()))
    tmp = list(map(int, input().split()))[:n]
    arr = [0] * (n + 1)
    arr[1:] = tmp[:]
    # print(arr)
    res = countGezi(arr, 1, h0, n)
    print(res % 998244353)


def countGezi(arr, i, hi, n):
    # count = 0
    if i > n:
        return 0
    if i == n:
        return 1
    # way1 = countGezi(arr, i + hi, hi, n)
    # way2 = countGezi(arr, i + arr[i], arr[i], n)

    # count += countGezi(arr, i + hi, hi, n) + countGezi(arr, i + arr[i], arr[i], n)

    # return way1 + way2
    return countGezi(arr, i + hi, hi, n) + countGezi(arr, i + arr[i], arr[i], n)
    # return count


if __name__ == '__main__':
    fun1()
