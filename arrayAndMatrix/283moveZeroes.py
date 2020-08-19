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

# 另一种思路
# 先遍历一遍数组，找到最后一个零所在的位置p；
# 用两个指针，一个指向位置p的指针p，一个指向数组末尾q
# 移动p，没找到一个零与末尾元素进行交换
