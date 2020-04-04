'''
@Time    : 2020/2/14 21:36
@FileName: 53maxSubArray.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # res = [0 for _ in range(len(nums))]
        # res[0] = nums[0]
        # for i in range(1, len(nums)):
        #     res[i] = max(nums[i], nums[i] + res[i - 1])
        # return max(res)
        res = nums[0]
        temp = nums[0]
        for i in range(1, len(nums)):
            temp = max(temp + nums[i], nums[i])
            res = max(res, temp)
        return res


if __name__ == '__main__':
    print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
