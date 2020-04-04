'''
@Time    : 2020/3/17 10:10
@FileName: 53maxSubArray.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


# 利用动态规划思想解决
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = [0 for _ in range(len(nums))]
        res[0] = nums[0]
        for i in range(1, len(nums)):
            res[i] = max(nums[i], nums[i] + res[i - 1])
        return max(res)
        # 对上述程序进行有序，降低空间复杂度
        # res = nums[0]
        # temp = nums[0]
        # for i in range(1, len(nums)):
        #     temp = max(temp + nums[i], nums[i])
        #     res = max(res, temp)
        # return res
