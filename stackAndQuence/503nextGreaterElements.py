'''
@Time    : 2020/3/4 11:58
@FileName: 503nextGreaterElements.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [-1 for _ in range(len(nums))]
        indexs = []
        lenNums = len(nums)
        for i in range(lenNums * 2):
            num = nums[i % lenNums]
            while indexs and nums[indexs[-1]] < num:
                res[indexs.pop()] = num
            if i < lenNums:
                indexs.append(i)
        return res
