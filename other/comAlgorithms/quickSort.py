"""
@Time    : 2020/3/23 15:37
@FileName: quickSort.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""
import time


# nums = [4, 2, 5, 3, 8]
# lo = 0
# hi = len(nums) - 1
# 经典快排，每次只能确定一个位置
def qucikSort(nums, lo, hi):
    # if lo < hi:
    #     privot = partition(nums, lo, hi)
    #     qucikSort(nums, lo, privot - 1)
    #     qucikSort(nums, privot + 1, hi)
    # return nums
    # time.time()
    if lo >= hi:
        return 0
    privot = partition(nums, lo, hi)
    qucikSort(nums, lo, privot - 1)
    qucikSort(nums, privot + 1, hi)
    return nums


def partition(nums, lo, hi):
    i = lo
    while lo < hi:
        while lo < hi and nums[hi] >= nums[i]:
            hi -= 1
        while lo < hi and nums[lo] <= nums[i]:
            lo += 1
        nums[lo], nums[hi] = nums[hi], nums[lo]
    nums[i], nums[hi] = nums[hi], nums[i]
    return hi


import random


# 改进后的快排 + 随机快排
def quickSort1(nums, lo, hi):
    # 判断程序执行时长
    # time.time()
    if lo >= hi:
        return 0
    swap(nums, lo + int(random.random() * (hi - lo + 1)), hi)
    p = partition1(nums, lo, hi)
    quickSort1(nums, lo, p[0] - 1)
    quickSort1(nums, p[1] + 1, hi)
    return nums


def partition1(nums, lo, hi):
    less = lo - 1
    more = hi
    # tem = nums[hi]
    while lo < more:
        if nums[lo] < nums[hi]:
            less += 1
            swap(nums, less, lo)
            lo += 1
        elif nums[lo] > nums[hi]:
            more -= 1
            swap(nums, more, lo)
        else:
            lo += 1
    swap(nums, more, hi)
    return [less + 1, more]


def quickSort3(nums, lo, hi):
    # 判断程序执行时长
    # time.time()
    if lo >= hi:
        return 0
    # swap(nums, lo + int(random.random() * (hi - lo + 1)), hi)
    p = partition1(nums, lo, hi)
    quickSort1(nums, lo, p[0] - 1)
    quickSort1(nums, p[1] + 1, hi)
    return nums


def swap(nums, lo, hi):
    nums[lo], nums[hi] = nums[hi], nums[lo]


if __name__ == '__main__':
    # nums = [1, 2, 3, 7, 6, 1, 2, 0, 1, 1]
    nums = [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    # nums = input().strip()
    # nums = list(map(int, nums.split(",")))
    lo = 0
    hi = len(nums) - 1
    # 1
    start_tm1 = time.time()
    print(qucikSort(nums, lo, hi))
    print(time.time() - start_tm1)
    # 2
    start_tm2 = time.time()
    print(quickSort1(nums, lo, hi))
    print(time.time() - start_tm2)

    # 3
    start_tm3 = time.time()
    print(quickSort3(nums, lo, hi))
    print(time.time() - start_tm3)

    # 执行速度
    # 2 > 3 >1
