'''
@Time    : 2020/4/16 14:44
@FileName: 5.6test01.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


def fun1():
    n, m = list(map(int, input().split()))
    nList = input()
    nList = list(map(int, nList.split()))[:n]
    count = 0
    while True:
        # while True:
        i = 1
        countA = 0
        if nList[i] > nList[i - 1]:
            Max = nList[i]
            countA += 1
            count += 1
            nList.append(nList.pop(i - 1))
            while True:
                i = 0
                if countA >= m:
                    return count
                if nList[i] > nList[i + 1]:
                    countA += 1
                    count += 1
                    nList.append(nList.pop(i + 1))
                else:
                    break
        else:
            countA += 1
            count += 1
            nList.insert(-1, nList.pop(i))
            while True:
                i = 0
                if countA >= m:
                    return count
                if nList[i] > nList[i + 1]:
                    countA += 1
                    count += 1
                    nList.append(nList.pop(i + 1))
                else:
                    break


if __name__ == '__main__':
    print(fun1())
