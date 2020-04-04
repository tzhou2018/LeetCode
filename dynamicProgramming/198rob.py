'''
@Time    : 2020/2/15 18:47
@FileName: 198rob.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


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


if __name__ == '__main__':
    print(Solution().rob([1, 2, 3, 1]))
