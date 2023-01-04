'''
@Time    : 2020/3/17 13:40
@FileName: 540singleNonDuplicate.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''
"""
思路：
我们首先将 lo 和 hi 指向数组首尾两个元素。然后进行二分搜索将数组搜索空间减半，
直到找到单一元素或者仅剩一个元素为止。当搜索空间只剩一个元素，则该元素就是单个元素。
在每个循环迭代中，我们确定 mid，变量 halvesAreEven = (hi - mid) % 2 == 0。
通过查看中间元素同一元素为哪一个（左侧子数组中的最后一个元素或右侧子数组中的第一个元素），
我们可以通过变量 halvesAreEven 确定现在哪一侧元素个数为奇数，并更新 lo 和 hi。
最难的部分是根据 mid 和 halvesAreEven 的值正确更新 lo 和 hi

作者：LeetCode
链接：https://leetcode-cn.com/problems/single-element-in-a-sorted-array/solution/you-xu-shu-zu-zhong-de-dan-yi-yuan-su-by-leetcode/

"""


class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            isEven = (hi - mid) % 2 == 0
            if nums[mid] == nums[mid + 1]:
                if isEven:
                    lo = mid + 2
                else:
                    hi = mid - 1
            elif nums[mid] == nums[mid - 1]:
                if isEven:
                    hi = mid - 2
                else:
                    lo = mid + 1
            else:
                return nums[mid]
        return nums[lo]

    # 方法2
    # 思路：遍历数组进行异或运算
    def singleNonDuplicate1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            res ^= num
        return res


if __name__ == '__main__':
    res = Solution().singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8])
    print(res)
