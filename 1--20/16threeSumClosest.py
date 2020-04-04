'''
@Time    : 2020/2/12 21:28
@FileName: 16threeSumClosest.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 同上一道题，使用双指针，遍历 nums 数组，取当前三个数值的和sum,
        # 求 sum 到target 的距离，也即接近程度。
        # 当当前数字相关的三个数值和 sum与target 距离更近时，更新距离（diff）
        # 最后保留的sum也就是最接近目标值。
        res = 0
        nums.sort()
        diff = float("inf")
        for i in range(len(nums)):
            start, end = i + 1, len(nums) - 1
            while start < end:
                i_sum = nums[i] + nums[start] + nums[end]
                if i_sum < target:
                    if abs(i_sum - target) < diff:
                        diff = abs(i_sum - target)
                        res = i_sum
                    start += 1
                else:
                    if abs(i_sum - target) < diff:
                        diff = abs(i_sum - target)
                        res = i_sum
                    end -= 1
        return res


if __name__ == '__main__':
    print(Solution().threeSumClosest([-1, 2, 1, -4], 1))
