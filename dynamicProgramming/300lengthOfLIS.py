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


"""
优化上述解法
构造dp数组时，可以使用二分法求解，时间效率为O(nlogn)
参考文章：程序员面试指南 P212
"""


class Solution2:
    def lengthOfLIS2(self, nums):
        if not nums:
            return 0
        dp = [1 for _ in range(len(nums))]
        # 辅助数组
        ends = [0 for _ in range(len(nums))]
        ends[0] = nums[0]
        right = 0
        for i in range(1, len(nums)):
            l = 0
            r = right
            # 利用二分法找到ends[0...right]有效区中大于等于arr[i]的位置
            while l <= r:
                m = (l + r) // 2
                if nums[i] > ends[m]:
                    l = m + 1
                else:
                    r = m - 1
            right = max(right, l)
            ends[right] = nums[i]
            dp[i] = right + 1
        return max(dp)



if __name__ == '__main__':
    print(Solution().lengthOfLIS([2, 1, 5, 3, 6, 4, 8, 9, 7]))
    print(Solution2().lengthOfLIS2([2, 1, 5, 3, 6, 4, 8, 9, 7]))
