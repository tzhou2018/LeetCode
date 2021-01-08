'''
@Time    : 2020/4/25 13:08
@FileName: 0425test01.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''
"""
钱老板放置广告牌
"""


def fun1():
    n = int(input().strip())
    arr = list(map(int, input().strip().split()[:n]))
    res1 = arr[0]
    Max1 = 0
    Min1 = float('inf')
    # count
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            res1 += res1
        if arr[i] != arr[i - 1]:
            res2 = min(arr[i], arr[i - 1])
            Min1 = min(res2, Min1)
            res1 = arr[i]
        Max1 = max(Max1, res1)

    print(max(Max1, Min1 * n))
    # print(resL)


if __name__ == '__main__':
    fun1()

    # res1 = arr[n - 1]
    # Max1 = 0
    # Min1 = float('inf')
    # # co
    # for i in range(len(arr) - 2, -1, -1):
    #     if arr[i] == arr[i + 1]:
    #         res1 += res1
    #     if arr[i] != arr[i + 1]:
    #         res2 = min(arr[i], arr[i + 1])
    #         Min1 = min(res2, Min1)
    #
    #         res1 = arr[i]
    #     Max1 = max(Max1, res1)
    # resR = max(Max1, Min1 * n)
    # print(max(resR, resL))

# def fun2():
#     n = int(input().strip())
#     if n > 100000:
#         print(0)
#         # return 0
#     else:
#         arr = list(map(int, input().strip().split()[:n]))
#         Max = 0
#
#         for i in range(1, n):
#             # left
#             res = arr[i]
#             temp = arr[i]
#             iL = i - 1
#             iR = i + 1
#             while iL >= 0:
#                 if temp <= arr[iL]:
#                     res += temp
#                     iL -= 1
#                 else:
#                     break
#             while iR < n:
#                 if temp <= arr[iR]:
#                     res += temp
#                     iR += 1
#                 else:
#                     break
#             Max = max(Max, res)
#         print(Max)
#     # return Max
