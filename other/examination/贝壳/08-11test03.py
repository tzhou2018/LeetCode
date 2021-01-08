"""
@Time    : 2020/8/11 19:35
@FileName: 08-11test03.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""

# 最xiao子区间做或运算，求具有最大值的的子区间的最小长度
def test03(arr):
    arrLen = len(arr)
    maxOr = 0
    indexMax = 0
    Max = arr[0]
    for i in range(arrLen):
        maxOr |= arr[i]
        if arr[i] >= Max:
            indexMax = i
            Max = arr[i]
    resLen = arrLen
    for i in range(arrLen):
        temp = 0
        for j in range(i, arrLen):

            temp |= arr[j]
            if temp >= maxOr:
                # maxOr = temp
                resLen = min(resLen, j - i + 1)
    return resLen
# 牛课上可以通过的写法
def third():
    n = int(input())
    nums = list(map(int, input().split(' ')))
    res = 0
    for i in nums:
        res = res | i
    length = len(nums)

    end = 0
    temp = 0
    for i in range(len(nums)):
        temp = temp | nums[i]
        if temp == res:
            end = i
            break

    for i in range(end, len(nums)):
        temp = 0
        for j in range(i, -1, -1):
            temp = temp | nums[j]
            if temp == res:
                length = min(length, i - j + 1)
                break

    print(length)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split(" ")[:n]))
    # arr = [1, 2, 3]
    print(test03(arr))
