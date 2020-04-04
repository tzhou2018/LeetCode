'''
@Time    : 2020/2/16 14:14
@FileName: 26removeDuplicates.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        lenNums = len(nums) - 1
        start = 0
        while start < lenNums:
            if nums[start] != nums[start + 1]:
                start += 1
            while start < lenNums and nums[start] == nums[start + 1]:
                nums.pop(start + 1)
                lenNums = len(nums) - 1
                # start += 1

        print(nums)
        return len(nums)

    # 方法 2
    # 无需删除 nums 中的元素
    def removeDuplicatesII(self, nums):
        if len(nums) <= 1:
            return len(nums)
        slow = 0
        for i in range(1, len(nums)):
            if nums[slow] != nums[i]:
                slow += 1
                nums[slow] = nums[i]
        print(nums)
        return slow + 1


if __name__ == '__main__':
    print(Solution().removeDuplicatesII([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
