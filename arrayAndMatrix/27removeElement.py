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
        if not  nums:
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


if __name__ == '__main__':
    print(Solution().removeElement([1], 1))
