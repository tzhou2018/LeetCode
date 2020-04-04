'''
@Time    : 2020/2/6 20:23
@FileName: twoSum.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 使用字典
        # if not nums:
        #     return None
        # result = {}
        # for index, value in enumerate(nums):
        #     anotherNum = target - value
        #     if anotherNum in result:
        #         return [result.get(anotherNum), index]
        #     result[value] = index
        # return None
        # 使用列表
        if not nums:
            return None
        result = []
        for i in range(len(nums) - 1):
            result.append(nums[i])
            if target - nums[i + 1] in result:
                return [result.index(target - nums[i + 1]), i + 1]
        return None


if __name__ == '__main__':
    print(Solution().twoSum([2, 3, 4, 5], 6))
