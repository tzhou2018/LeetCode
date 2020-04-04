'''
@Time    : 2020/3/8 20:44
@FileName: 645findErrorNums.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(nums)
        if size < 2:
            return []
        for i in range(size):
            while i + 1 != nums[i] and nums[i] != nums[nums[i] - 1]:
                self.__swap(nums, i, nums[i] - 1)
        for i in range(size):
            if nums[i] != i + 1:
                return [nums[i], i + 1]

    def __swap(self, nums, index1, index2):
        if index1 == index2:
            return
        temp = nums[index1]
        nums[index1] = nums[index2]
        nums[index2] = temp
