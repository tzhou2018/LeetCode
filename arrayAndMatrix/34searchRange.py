'''
@Time    : 2020/2/16 19:21
@FileName: 34searchRange.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums or target not in nums:
            return [-1, -1]
        right = len(nums) - 1
        left = 0
        # 获取左索引
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        leftIndex = left
        # 获取右索引
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        rightIndex = right
        return [leftIndex, rightIndex]

    # 参考荷兰国旗的解法，时间复杂度O(n)
    def searchRange1(self, arr, target):
        if not arr or target not in arr:
            return [-1, -1]
        if min(arr) > target:
            return [-1, -1]
        lo = 0
        hi = len(arr)
        less = lo - 1
        most = hi
        while lo < most:
            if arr[lo] < target:
                less += 1
                # self.swap(arr, less, lo)
                lo += 1
            elif arr[lo] > target:
                break
            else:
                lo += 1
        print(arr)
        return [less + 1, lo - 1]

    def swap(self, arr, start, end):
        arr[start], arr[end] = arr[end], arr[start]


if __name__ == '__main__':
    # print(Solution().searchRange([5, 7, 7, 8, 8, 10], 1))
    print(Solution().searchRange1([5, 7, 7, 8, 8, 10], 7))
