'''
@Time    : 2020/2/15 19:21
@FileName: 213robII.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


# 此题中，我们将第一家与最后一家分开。此时问题同 robI ,
# 只需计算 nums[0:n-1] nums[1:n] 中的最大值即可。

class Solution(object):
    def robII(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        lenNums = len(nums)
        return max(self.robI(nums[0:lenNums - 1]), \
                   self.robI(nums[1:lenNums]))

    def robI(self, nums):
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


if __name__ == '__main__':
    print(Solution().robII([1]))
