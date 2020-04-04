'''
@Time    : 2020/3/19 19:46
@FileName: meituan2.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


def maxScore():
    input1 = input()
    n, k, m = list(map(int, input1.split()))
    input2 = input()
    p, q = list(map(int, input2.split()))
    input3 = input()
    time = list(map(int, input3.split()))
    time.sort()
    res = 0
    flag = True
    for i in range(n):
        for j in range(k):
            if m >= time[j]:
                res += p
                m -= time[j]
                flag = True
            elif time[j - 1] <= m <= time[j]:
                flag = False
                continue
            else:
                flag = False
                break

        if flag:
            res += q
        else:
            continue
    return res


if __name__ == '__main__':
    print(maxScore())
