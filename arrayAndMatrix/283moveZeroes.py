'''
@Time    : 2020/3/8 15:52
@FileName: 283moveZeroes.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''

# 思路：
# 先将非零元素放在移动到列表前面，之后列表尾部用零补全
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        index = 0
        numsLen = len(nums)
        for num in nums:
            if num != 0:
                nums[index] = num
                index += 1
        while index < numsLen:
            nums[index] = 0
            index += 1
        return nums
