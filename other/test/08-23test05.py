"""
@Time    : 2020/3/23 15:37
@FileName: quickSort.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""


# nums = [4, 2, 5, 3, 8]
# lo = 0
# hi = len(nums) - 1

# https://blog.csdn.net/ZT7524/article/details/102761502
# 经典快排，每次只能确定一个位置
def qucikSort(nums, lo, hi):
    # if lo < hi:
    #     privot = partition(nums, lo, hi)
    #     qucikSort(nums, lo, privot - 1)
    #     qucikSort(nums, privot + 1, hi)
    # return nums
    if lo >= hi:
        return 0
    privot = partition(nums, lo, hi)
    # privot = 6
    #
    qucikSort(nums, lo, privot - 1)  # qucikSort(nums, 0, 6 - 1) 左边的部分 nums = [11, 32, 3, 4, 1, 8,]

    qucikSort(nums, privot + 1, hi)  # qucikSort(nums, 7, 7) 右边这部分 nums = [89]
    return nums


"""
# 思考题？
1. 经典快排每次确定一个元素，那么，若快排的基准元素存在多个，我们如何通过一趟快排确定所有的基准元素？
    nums = [50，50，50, 32, 3, 4,67，67， 1, 8, 11, 89]
    
2. 快速适用的场景？
提示： 当所排序列满足哪种情形时适用快排合适？

"""


# 思考题？
# 1. 经典快排每次确定一个元素，那么，若快排的基准元素存在多个，我们如何通过一趟快排确定所有的基准元素？
# nums = [50，50，50, 32, 3, 4,67，67， 1, 8, 11, 89]


# # 一次比较
#  0,1,2,3,4,5,6,7
# nums = [50, 32, 3, 4, 1, 8, 11, 89]
#
# # hi  = 6
#
# # lo = 6
#
# nums = [11, 32, 3, 4, 1, 8, 50, 89]


def partition(nums, lo, hi):
    i = lo  # 基准元素
    while lo < hi:
        while lo < hi and nums[hi] >= nums[i]:
            hi -= 1
        while lo < hi and nums[lo] <= nums[i]:  # nums[i] 是基准元素，若是i不发生变化，那么num[i]永远不变
            lo += 1
        nums[lo], nums[hi] = nums[hi], nums[lo]
    nums[i], nums[hi] = nums[hi], nums[i]
    return hi


import random


# 改进后的快排 + 随机快排
def quickSort1(nums, lo, hi):
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


def swap(nums, lo, hi):
    nums[lo], nums[hi] = nums[hi], nums[lo]


if __name__ == '__main__':
    nums = [1, 2, 3, 7, 6, 1, 2, 0, 1, 1]
    # nums = input().strip()
    # nums = list(map(int, nums.split(",")))
    lo = 0
    hi = len(nums) - 1
    print(qucikSort(nums, lo, hi))
    # print(quickSort1(nums, lo, hi))
