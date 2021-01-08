'''
@Time    : 2020/2/16 14:53
@FileName: 27removeElement.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        lenNums = len(nums) - 1
        start = 0
        while start <= lenNums:
            if nums[start] != val:
                start += 1
            else:
                nums.pop(start)
                lenNums = len(nums) - 1
        # print(nums)
        return len(nums)

    # 方法2
    # 思路同26题中的方法2
    def removeElement2(self, nums, val):
        if not nums:
            return 0
        slow = 0
        lenNums = len(nums)
        for i in range(lenNums):
            if nums[i] != val:
                nums[slow] = nums[i]
                slow += 1
        # print(nums)
        return slow


if __name__ == '__main__':
    print(Solution().removeElement2([0, 1, 2, 2, 3, 0, 4, 2], 2))
