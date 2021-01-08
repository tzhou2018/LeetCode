"""
@Time    : 2020/8/12 9:15
@FileName: 08-12test02.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""


def test():
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    res = []
    for i in range(n):
        binaryTemp = arr[i]
        binaryNum = bin(binaryTemp)
        minRes = arr[i]
        binary1 = binaryNum.count("1")
        for i in range(binaryTemp, binaryTemp // 2, -1):
            temp = bin(i)
            if len(temp) == len(binaryNum) and temp.count("1") > binary1:
                binary1 = temp.count("1")
                minRes = min(minRes, i)
        res.append(minRes)
    for i in range(n):
        print(res[i])


# def count1(arr):
#     return arr.count("1")

if __name__ == '__main__':
    test()
