'''
@Time    : 2020/3/19 13:41
@FileName: 462minMoves2.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''
"""
方法1：先排序
这是个典型的相遇问题，移动距离最小的方式是所有元素都移动到中位数。理由如下：

设 m 为中位数。a 和 b 是 m 两边的两个元素，且 b > a。要使 a 和 b 相等，
它们总共移动的次数为 b - a，这个值等于 (b - m) + (m - a)，
也就是把这两个数移动到中位数的移动次数。

设数组长度为 N，则可以找到 N/2 对 a 和 b 的组合，使它们都移动到 m 的位置。
"""


class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        move = 0
        start = 0
        end = len(nums) - 1
        nums.sort()
        while start <= end:
            move += nums[end] - nums[start]
            end -= 1
            start += 1
        return move


# 方法2
# 使用快排先确定中位数
class Solution1(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsLen = len(nums)
        k = self.findKthLargeset(nums, numsLen // 2)
        print(k)
        move = 0
        for num in nums:
            move += abs(num - k)
        return move

    def findKthLargeset(self, nums, k):
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            pivot = self.partition(nums, lo, hi)
            if k == pivot:
                break
            elif pivot < k:
                lo = pivot + 1
            else:
                hi = pivot - 1
        print(nums)
        return nums[k]

    def partition(self, nums, lo, hi):
        i = lo
        while lo < hi:

            while lo < hi and nums[hi] >= nums[i]:
                hi -= 1
            while lo < hi and nums[lo] <= nums[i]:
                lo += 1
            nums[lo], nums[hi] = nums[hi], nums[lo]
        nums[i], nums[hi] = nums[hi], nums[i]

        return hi


if __name__ == '__main__':
    print(Solution1().minMoves2([1, 2, 3]))
