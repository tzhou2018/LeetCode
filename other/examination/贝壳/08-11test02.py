"""
@Time    : 2020/8/11 20:21
@FileName: 08-11test02.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""
# 染色，每种颜色染的格子要一样

def test():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().strip().split(" "))))
    for i in range(n):
        allNum = arr[i][0] * arr[i][1]
        if allNum % 2 == 0:
            print(2)
        elif allNum % 3 == 0:
            print(3)
        elif allNum % 5 == 0:
            print(5)
        elif allNum == 1:
            print(1)
        elif allNum % 7 == 0:
            print(7)
        elif arr[i][0] == arr[i][1]:
            print(arr[i][0])
        else:
            print(allNum)


if __name__ == '__main__':
    test()
