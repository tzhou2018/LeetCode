"""
@Time    : 2020/3/17 14:47
@FileName: 34searchRange.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""


# 思路
# 采用两次二分查找，求出区间左右索引
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums or target not in nums:
            return [-1, -1]
        right = len(nums) - 1
        left = 0
        # 获取左索引
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        leftIndex = left
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        rightIndex = right
        return [leftIndex, rightIndex]
