'''
@Time    : 2020/3/19 20:43
@FileName: meituan3.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''
"""
用dp数组记录不跳跃的连续上升长度，用res数组记录可跳跃的最大上升长度，
然后如果nums[i]>nums[i-1]，nums[i]=nums[i-1]+1，然后判断如果nums[i]>nums[i-2]，
res[i] = max(res[i],dp[i-2]+1)，这里一定是dp[i-2]，因为跳过了第i-1个数，
那么之前的连续上升长度是未跳跃过的
"""


def length():
    # n = int(input())
    # nums = input()
    # nums = list(map(int, nums.split()))[:n]
    nums = [2, 1, 3, 2, 5]
    lenNums = len(nums)
    dp = [1 for _ in range(lenNums)]
    res = [1 for _ in range(lenNums)]
    maxSubList = 1
    for i in range(lenNums):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[j] + 1, dp[i])
        maxSubList = max(maxSubList, dp[i])
    print(dp)
    for j in range(1, lenNums):
        if nums[j] > nums[j - 1]:
            res[j] = res[j - 1] + 1
        if j >= 2 and nums[j] > nums[j - 2]:
            res[j] = max(res[j], dp[j - 2] + 1)
    return max(res)


if __name__ == '__main__':
    print(length())
