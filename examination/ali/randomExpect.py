'''
@Time    : 2020/3/28 10:29
@FileName: randomExpect.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''

import sys

"""
解题思路：暴力破解
首先找到n个随机数的所有情况
然后找到最小值的范围
然后寻找每个可能值可能出现的次数并计算概率, 更新期望:
依次让第i个随机数为num，统计可能的出现的次数
在统计其他位置可能的情况的时候，要略过已经统计过的情况（见代码）
"""


def func(N, LS, RS):
    # 首先找到n个随机数的所有情况
    total = 1
    for i in range(N):
        total *= (RS[i] - LS[i]) + 1

    # 然后找到最小值的范围
    min_num = min(LS)
    max_num = min(RS)

    ans = 0
    # 然后寻找每个可能值的概率, 并计算期望: 依次让第i个随机数为num，统计可能的出现的次数
    for num in range(min_num, max_num + 1):
        count = 0
        for i in range(N):
            tmp = 1
            if LS[i] <= num <= RS[i]:  # 第i个随机数可以取到num才计算：
                for j in range(N):
                    if j != i:  # 统计其他位置可能的情况
                        if j < i and LS[j] <= num:  # 略过已经统计过的情况
                            pro = min(RS[j] - LS[j], RS[
                                j] - num)  # 例如：示例中统计最小值为2的情况时，取第一位为2，有(2, 2),(2,3);
                            # 取第二位为2时，应略过(2, 2), 此时只有(3,2)
                        else:
                            pro = min(RS[j] - LS[j], RS[j] - num) + 1
                        tmp *= pro
            else:
                tmp = 0
            count += tmp
        p = count / total  # 计算概率
        ans += num * p  # 更新期望
    return ans


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    line = sys.stdin.readline().strip()
    ls = list(map(int, line.split()))
    line = sys.stdin.readline().strip()
    rs = list(map(int, line.split()))
    print(func(n, ls, rs))
