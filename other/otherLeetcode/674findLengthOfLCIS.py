"""
@Time    : 2020/7/29 21:43
@FileName: 674findLengthOfLCIS.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""


def findLengthOfLCIS(arr):
    if not arr:
        return 0
    ans = 1
    flag = -1
    for i in range(1, len(arr)):
        if arr[i - 1] >= arr[i]:
            flag = i - 1
        ans = max(ans, i - flag)
    return ans


if __name__ == '__main__':
    res = findLengthOfLCIS([1, 3, 5, 4, 7])
    print(res)
