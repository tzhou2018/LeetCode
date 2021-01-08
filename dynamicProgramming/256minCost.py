'''
@Time    : 2020/2/15 16:30
@FileName: 256minCost.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


# 只有三种颜色（三列），在保证相邻两个房子粉刷颜色不同的情况下，
# 求出这三列元素的粉刷完成的总价格。
class Solution(object):
    def minCost(self, nums):
        if not nums:
            return 0
        if len(nums[0]) == 0:
            return 0
        rows = len(nums)
        dp = [[0] * 3 for _ in range(rows)]
        dp[0] = nums[0]
        for i in range(1, rows):
            dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + nums[i][0]
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + nums[i][1]
            dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + nums[i][2]
        return min(dp[-1])


if __name__ == '__main__':
    print(Solution().minCost([[17, 2, 17], [16, 16, 5], [14, 3, 19]]))
