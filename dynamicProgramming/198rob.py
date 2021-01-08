'''
@Time    : 2020/2/15 18:47
@FileName: 198rob.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


# 方法1
# 动态规划
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) < 2:
            return nums[-1]
        lenNums = len(nums)
        dp = [0 for _ in range(lenNums)]
        dp[0] = nums[0]
        dp[1] = nums[0] if nums[0] > nums[1] else nums[1]
        for i in range(2, lenNums):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[lenNums - 1]


# 递归+记忆搜索
"""
参考文章
https://leetcode-cn.com/problems/house-robber/solution/dong-tai-gui-hua-zen-yao-xiang-xian-di-gui-ji-yi-h/
"""


class Solution2:
    def rob(self, nums):
        if not nums:
            return 0
        return self.recursionRob(nums, len(nums) - 1)
        pass

    def recursionRob(self, nums, i):
        if i == 0:
            return nums[i]
        if i == 1:
            return max(nums[0], nums[1])
        return max(self.recursionRob(nums, i - 1), self.recursionRob(nums, i - 2) + nums[i])

    # 上述解法时间复杂度较高，因为在计算i位置获得的金额时做了重复计算，
    # 因此，可以将i位置计算的结果保存下来.
    # 采用记忆化搜索
    def improveRob(self, nums):
        if not nums:
            return 0
        self.res = {}
        return self.improveRecursionRob(nums, len(nums) - 1)

    def improveRecursionRob(self, nums, i):
        if i in self.res:
            return self.res[i]
        temp = 0
        if i == 0:
            temp = nums[i]
        elif i == 1:
            temp = max(nums[0], nums[1])
        else:
            temp = max(self.improveRecursionRob(nums, i - 1), self.improveRecursionRob(nums, i - 2) + nums[i])
        self.res[i] = temp
        return temp


if __name__ == '__main__':
    print(Solution().rob([1, 2, 3, 1]))
    # 递归 + 记忆化搜索
    print(Solution2().rob([1, 2, 3, 1]))
    print(Solution2().improveRob([1, 2, 3, 1]))
