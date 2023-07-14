"""
@Time    : 2020/3/15 15:45
@FileName: 167twoSum.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""

"""
使用双指针，一个指针指向值较小的元素，一个指针指向值较大的元素。
指向较小元素的指针从头向尾遍历，指向较大元素的指针从尾向头遍历。

如果两个指针指向元素的和 sum == target，那么得到要求的结果；
如果 sum > target，移动较大的元素，使 sum 变小一些；
如果 sum < target，移动较小的元素，使 sum 变大一些。
数组中的元素最多遍历一次，时间复杂度为 O(N)。只使用了两个额外变量，空间复杂度为 O(1)。
"""


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        right = len(numbers) - 1
        left = 0
        while left < right:
            sums = numbers[left] + numbers[right]
            if sums == target:
                return [left + 1, right + 1]
            elif sums > target:
                right -= 1
            else:
                left += 1
        return None
