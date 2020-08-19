'''
@Time    : 2020/2/15 16:30
@FileName: 256minCost.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


# 大体思路同上一题
# 本题中，我们从第 i 间屋子开始，i > 0;
# 取 i-1 间屋子所图颜料的最小值 min1 以及次小值 min2，
# 判断 第 i 间屋子的颜色与第 i -1 间屋子的颜色是否重合
# 不重合：则第 i 间屋子最小花费为 nums[i][j] + min1
# 否则：第 i 间屋子最小花费为 nums[i][j] + min2

class Solution(object):
    def minCostII(self, nums):
        if len(nums) == 0 or len(nums[0]) == 0:
            return 0
        rows = len(nums)
        cols = len(nums[0])
        dp = [[1] * cols for _ in range(rows)]
        dp[0] = nums[0]
        for i in range(1, rows):
            temp = sorted(dp[i - 1])
            min1, min2 = temp[0], temp[1]
            for j in range(cols):

                if j != dp[i - 1].index(min1):
                    dp[i][j] = min1 + nums[i][j]
                else:
                    dp[i][j] = min2 + nums[i][j]
        return min(dp[-1])


if __name__ == '__main__':
    print(Solution().minCostII([[1, 5, 3], ]))
