'''
@Time    : 2020/3/15 19:50
@FileName: 88merge.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


# 需要从尾开始遍历，否则在 nums1 上归并得到的值会覆盖还未进行归并比较的值。
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        mergeIndex = m + n - 1
        index1 = m - 1
        index2 = n - 1
        while index1 >= 0 and index2 >= 0:
            if nums1[index1] >= nums2[index2]:
                nums1[mergeIndex] = nums1[index1]
                index1 -= 1
                mergeIndex -= 1
            else:
                nums1[mergeIndex] = nums2[index2]
                index2 -= 1
                mergeIndex -= 1
        while index1 >= 0:
            nums1[mergeIndex] = nums1[index1]
            index1 -= 1
            mergeIndex -= 1
        while index2 >= 0:
            nums1[mergeIndex] = nums2[index2]
            index2 -= 1
            mergeIndex -= 1
        return nums1

    def merge2(self, nums1, m, nums2, n):
        mergeIndex = m + n - 1
        index1 = m - 1
        index2 = n - 1
        while index1 >= 0 or index2 >= 0:
            if index1 < 0:
                nums1[mergeIndex] = nums2[index2]
                index2 -= 1
                mergeIndex -= 1
            elif index2 < 0:
                nums1[mergeIndex] = nums1[index1]
                index1 -= 1
                mergeIndex -= 1
            elif nums1[index1] >= nums2[index2]:
                nums1[mergeIndex] = nums1[index1]
                index1 -= 1
                mergeIndex -= 1
            else:
                nums1[mergeIndex] = nums2[index2]
                index2 -= 1
                mergeIndex -= 1
        return nums1
