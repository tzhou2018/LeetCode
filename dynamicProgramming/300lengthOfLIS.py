'''
@Time    : 2020/2/15 15:25
@FileName: 300lengthOfLIS.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        lenNums = len(nums)
        dp = [1 for _ in range(lenNums)]
        maxSubList = 1
        for i in range(lenNums):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
            maxSubList = max(maxSubList, dp[i])
        print(dp)
        return maxSubList


if __name__ == '__main__':
    print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
