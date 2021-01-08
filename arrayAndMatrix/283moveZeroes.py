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


# 方法2
# 这里可以参照双指针的思路解决，指针j是一直往后移动的，如果指向的值不等于0才对他进行操作。
# 指针i 记录走过的非零元素
def moveZeroes(nums):
    i: int = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    return nums


if __name__ == '__main__':
    print(moveZeroes([0, 1, 0, 3, 12]))
