'''
@Time    : 2020/3/20 14:27
@FileName: 238productExceptSelf.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


# 思路
# 依次从左从右遍历所给nums,即，计算res[i]时，
# 先计算i左边的所有元素乘积，在乘以右边的所有元素乘积。
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lenNums = len(nums)
        res = [1] * lenNums
        left = 1
        for i in range(1, lenNums):
            left *= nums[i - 1]
            res[i] *= left
        right = 1
        for j in range(lenNums - 2, -1, -1):
            right *= nums[j + 1]
            res[j] *= right
        return res
