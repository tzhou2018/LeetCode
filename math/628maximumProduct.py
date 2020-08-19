'''
@Time    : 2020/3/20 14:56
@FileName: 628maximumProduct.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    """
    # 方法1
    我们将数组进行升序排序，如果数组中所有的元素都是非负数，那么答案即为最后三个元素的乘积。
    如果数组中出现了负数，那么我们还需要考虑乘积中包含负数的情况，显然选择最小的两个负数和最大的
    一个正数是最优的，即为前两个元素与最后一个元素的乘积。
    上述两个结果中的较大值就是答案。注意我们可以不用判断数组中到底有没有正数，
    0 或者负数，因为上述两个结果实际上已经包含了所有情况，最大值一定在其中。

    """

    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])

    # 方法2
    # 在方法一中，我们实际上只要求出数组中最大的三个数以及最小的两个数，
    # 因此我们可以不用排序，用线性扫描直接得出这五个数。
    def maximumProduct2(self, nums):
        min1, min2 = float('inf'), float('inf')
        max1, max2, max3 = float('-inf'), float('-inf'), float('-inf')
        for num in nums:
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num
        return max(min1 * min2 * max1, max1 * max2 * max3)


if __name__ == '__main__':
    print(Solution().maximumProduct2([1, 2, 3]))
