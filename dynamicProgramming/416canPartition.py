"""
@Time    : 2020/8/9 11:28
@FileName: 416canPartition.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""
"""
参考文章：
https://leetcode-cn.com/problems/partition-equal-subset-sum/solution/0-1-bei-bao-wen-ti-xiang-jie-zhen-dui-ben-ti-de-yo/
"""
# 背包问题思路
from typing import List


class Solution:
    def canPartition(self, nums: List[int]):
        if not nums or len(nums) < 2:
            return False
        lenNums = len(nums)
        target = sum(nums)
        if target & 1:
            return False
        target = target >> 1
        dp = [[False] * (target + 1) for _ in range(lenNums)]
        for i in range(target + 1):
            dp[0][nums[0]] = True
        for i in range(1, lenNums):
            for j in range(1, target + 1):
                # 将上一行的复制过来
                dp[i][j] = dp[i - 1][j]
                if j == nums[i]:
                    dp[i][j] = True
                    continue
                if j > nums[i]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
        return dp[lenNums - 1][target]


if __name__ == '__main__':
    solution = Solution()
    print(solution.canPartition([1, 5, 6, 11]))
