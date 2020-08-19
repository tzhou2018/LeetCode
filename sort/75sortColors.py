'''
@Time    : 2020/3/16 14:46
@FileName: 75sortColors.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''
"""
思路：
我们用三个指针（p0, p2 和curr）来分别追踪0的最右边界，2的最左边界和当前考虑的元素。

本解法的思路是沿着数组移动 curr 指针，若nums[curr] = 0，则将其与 nums[p0]互换；若 nums[curr] = 2 ，则与 nums[p2]互换。

算法

初始化0的最右边界：p0 = 0。在整个算法执行过程中 nums[idx < p0] = 0.

初始化2的最左边界 ：p2 = n - 1。在整个算法执行过程中 nums[idx > p2] = 2.

初始化当前考虑的元素序号 ：curr = 0.

While curr <= p2 :

若 nums[curr] = 0 ：交换第 curr个 和 第p0个 元素，并将指针都向右移。

若 nums[curr] = 2 ：交换第 curr个和第 p2个元素，并将 p2指针左移 。

若 nums[curr] = 1 ：将指针curr右移。

作者：LeetCode
链接：https://leetcode-cn.com/problems/sort-colors/solution/yan-se-fen-lei-by-leetcode/
"""


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # p0 = cur = 0
        # p2 = len(nums) - 1
        # while cur <= p2:
        #     if nums[cur] == 0:
        #         nums[cur], nums[p0] = nums[p0], nums[cur]
        #         p0 += 1
        #         cur += 1
        #     elif nums[cur] == 2:
        #         nums[cur], nums[p2] = nums[p2], nums[cur]
        #         p2 -= 1
        #     else:
        #         cur += 1
        low = -1
        cur = 0
        high = len(nums)
        while cur < high:
            if nums[cur] == 0:
                low += 1
                nums[low], nums[cur] = nums[cur], nums[low]
                cur += 1
            elif nums[cur] == 2:
                high -= 1
                nums[cur], nums[high] = nums[high], nums[cur]
            else:
                cur += 1
        return nums


if __name__ == '__main__':
    print(Solution().sortColors([0, 1, 2, 1, 1, 1, 0, 2, 2, 0]))
