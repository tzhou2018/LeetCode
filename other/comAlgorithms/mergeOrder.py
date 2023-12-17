'''
@Time    : 2020/3/25 20:28
@FileName: mergeOrder.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


def mergesort1(seq):
    """归并排序"""
    if len(seq) <= 1:
        return seq
    mid = len(seq) // 2  # 将列表分成更小的两个列表
    # 分别对左右两个列表进行处理，分别返回两个排序好的列表
    left = mergesort1(seq[:mid])
    right = mergesort1(seq[mid:])
    # 对排序好的两个列表合并，产生一个新的排序好的列表
    return merge1(left, right)


def merge1(left, right):
    """合并两个已排序好的列表，产生一个新的已排序好的列表"""
    result = []  # 新的已排序好的列表
    i = 0  # 下标
    j = 0
    # 对两个列表中的元素 两两对比。
    # 将最小的元素，放到result中，并对当前列表下标加1
    count = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


#
#
# if __name__ == '__main__':
#     seq = [5, 3, 0, 6, 1, 4]
#     print('排序前：', seq)
#     result = mergesort(seq)
#     print('排序后：', result)
# 数组中的逆序对
# 解题思路：实质是考察归并排序
# -*- coding:utf-8 -*-
class Solution:
    def mergeSort(self, data):
        if not data or len(data) < 1:
            return 0
        return self.InversePairs(data, 0, len(data) - 1)

    def InversePairs(self, data, lo, hi):
        # write code here
        if lo == hi:
            return 0
        mid = lo + (hi - lo) // 2
        left = self.InversePairs(data, lo, mid)
        right = self.InversePairs(data, mid + 1, hi)
        res = self.Merge(data, lo, mid, hi)
        return left + right + res

        # temp 作为辅助数组，每次将temp中基本有序的元素赋值给 data，

    # data赋值给temp继续归并
    def Merge(self, data, low, mid, high):

        count = 0
        i = low
        j = mid + 1
        res = []
        while i <= mid and j <= high:
            if data[i] <= data[j]:
                res.append(data[i])
                i += 1
            else:
                res.append(data[j])
                count += mid - i + 1
                j += 1
        # 若第一个表未检测完， 复制
        while i <= mid:
            res.append(data[i])
            i += 1
        # 若第二个表未检测完， 复制
        while j <= high:
            res.append(data[j])
            j += 1
        # 将局部排序好的res 去 替换原数组arr
        data[low:high + 1] = res
        return count


if __name__ == '__main__':
    print(Solution().mergeSort([7, 5, 6, 4]))
