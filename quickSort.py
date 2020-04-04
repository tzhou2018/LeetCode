'''
@Time    : 2020/3/23 15:37
@FileName: quickSort.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''
nums = [4, 2, 5, 3, 8]
lo = 0
hi = len(nums) - 1


def qucikSort(nums, lo, hi):
    # if lo < hi:
    #     privot = partition(nums, lo, hi)
    #     qucikSort(nums, lo, privot - 1)
    #     qucikSort(nums, privot + 1, hi)
    # return nums
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


if __name__ == '__main__':
    print(qucikSort(nums, lo, hi))
