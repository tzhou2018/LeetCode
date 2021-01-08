"""
@Time    : 2020/8/1 15:27
@FileName: 08-1test01.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""
import itertools


class Solution:
    def reletive_7(self, arr):
        # write code here
        if not arr:
            return 0
        arr = map(str, arr)
        reverPer = itertools.permutations(arr)
        res = 0
        for e in reverPer:
            temp = int(''.join(e))
            if temp % 7 == 0:
                res += 1
        return res


if __name__ == '__main__':
    arr = input().strip()
    arr = arr[1:-1]
    arr = arr.split(",")
    arr = list(map(int, arr))
    print(Solution().reletive_7(arr))
