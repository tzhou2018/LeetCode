"""
@Time    : 2020/8/6 14:11
@FileName: 8-2test02.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""

import functools

# def test(o1, o2):
#     if o1[0] != o2[0]:
#         return o1[0] - o2[0]
#     else:
#         return o1[1] - o2[1]
from collections import defaultdict

n = int(input())
res = []

send = defaultdict(list)
for i in range(n):
    a, b = [int(i) for i in input().split(' ')]
    res.append(a)
    b -= 2
    send[b].append(i)


def getMaxValue(k):
    r = res[k]
    if k in send:
        for i in send[k]:
            r += getMaxValue(i)
    return max(r, 0) % 1000000003


a = 0
for i in range(n):
    a = max(getMaxValue(i), a)
print(a)

# if __name__ == '__main__':
#     arr = [[1, 4], [1, 2], [2, 3], [3, 4]]
#     # arr.sort(key=test)
#     arr.sort(key=functools.cmp_to_key(test))
#     print(arr)
# print(sorted(arr, key=functools.cmp_to_key(test)))
