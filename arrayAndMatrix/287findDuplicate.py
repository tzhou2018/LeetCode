'''
@Time    : 2020/3/9 17:35
@FileName: 287findDuplicate.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


# 二分查找解法：
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 1
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            count = 0
            for i in range(len(nums)):
                if nums[i] <= mid:
                    count += 1
            if count > mid:
                end = mid - 1
            else:
                start = mid + 1
        return start


# 双指针解法，类似于有环链表中找出环的入口：
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
