'''
@Time    : 2020/4/29 9:19
@FileName: 01FinTech.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''

import sys


class Solution:

    def fun1(self):
        # while True:
        n = int(input().strip())
        arr = sys.stdin.readline().strip()
        arr = list(map(int, arr.split()))
        Min = min(arr)
        Max = max(arr)
        if Min != 0 or Max != 2 * n - 1:
            return 0
        if n < 2 or len(arr) != 2 * n:
            return 0
        res = 0
        for i in range(1, 2 * n, 2):
            diff = arr[i] - arr[i - 1]
            if abs(diff) == 1:
                continue
            # if diff < 0:
            if arr[i] & 1 == 1:
                index1 = arr.index(arr[i] - 1)
                arr[i - 1], arr[index1] = arr[index1], arr[i - 1]
                res += 1
            else:
                index1 = arr.index(arr[i] + 1)
                arr[i - 1], arr[index1] = arr[index1], arr[i - 1]
                res += 1
        print(res)


if __name__ == '__main__':
    res = Solution().fun1()
    # print(res)
