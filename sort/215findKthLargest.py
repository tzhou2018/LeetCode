'''
@Time    : 2020/3/15 22:32
@FileName: 215findKthLargest.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''

# 使用快速排序
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        low = 0
        high = len(nums) - 1
        k = len(nums) - k
        while low < high:
            pivot = self.partition(nums, low, high)
            if pivot == k:
                break
            if pivot < k:
                low = pivot + 1
            if pivot > k:
                high = pivot -1
        print(nums)
        return nums[k]

    def partition(self, nums, low, high):
        i = low
        while low < high:
            while low < high and nums[high] >= nums[i]:
                high -= 1
            while low < high and nums[low] <= nums[i]:
                low += 1

            self.swap(nums, low, high)
        self.swap(nums, i, high)
        return high

    def swap(self, nums, low, high):
        nums[low], nums[high] = nums[high], nums[low]


if __name__ == '__main__':
    print(Solution().findKthLargest([1,2,3], 1))
