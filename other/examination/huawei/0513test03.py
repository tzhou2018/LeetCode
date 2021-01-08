"""
@Time    : 2020/5/13 20:15
@FileName: 0513test02.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""

"""
def fun1():
    book = int(input().strip())
    n = int(input().strip())
    res = []
    temp = []
    for _ in range(n):
        input3 = list(map(int, input().strip().split()))
        res.append(input3)
    temp.extend(res[0])
    result = 1
    for i in range(1, n):
        e = res[i]
        for j in e:
            if j not in temp:
                result += 1
                break
            else:
                continue
        temp.extend(e)
    print(result)


if __name__ == '__main__':
    fun1()

"""
def fun1():
    book = int(input().strip())
    n = int(input().strip())
    res = []
    temp = []
    for _ in range(n):
        input3 = list(map(int, input().strip().split()))
        res.append(input3)
    temp.extend(res[0])
    result = n
    for i in range(1, n):
        e = res[i]
        for j in e:
            if j not in temp:
                # result += 1
                # break
                continue
            else:
                result -= 1
                break
                # continue
        temp.extend(e)
    print(result)


if __name__ == '__main__':
    fun1()
