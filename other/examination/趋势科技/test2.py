'''
@Time    : 2020/5/7 21:09
@FileName: test2.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


def fun1():
    arr = list(range(1, 12))
    start = 0
    k = 1
    while len(arr) > 1:
        out = (start + k) % len(arr)
        value = arr[(out + 1) % len(arr)]
        print(arr[out], end='\t')
        del (arr[out])
        k += 1
        start = arr.index(value)
    return arr[0]


def getIndex(arr, value):
    return arr.index(value)


if __name__ == '__main__':
    print(fun1())
