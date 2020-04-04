'''
@Time    : 2020/3/28 21:11
@FileName: 47permuteUnique.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''

"""
和46题不同的是一定要注意剪枝条件，参考下面的链接，很棒的讲解
https://leetcode-cn.com/problems/permutations-ii/solution/hot-100-47quan-pai-lie-ii-python3-hui-su-kao-lu-zh/
"""
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        check = [0] * len(nums)
        nums.sort()
        self.backTracking(nums, check, [])
        return self.res

    def backTracking(self, nums, check, path):
        if len(path) == len(nums):
            self.res.append(path)
            return
        for i in range(len(nums)):
            if check[i] == 1:
                continue
            # 如果当前元素与上一个元素相等，并且上一次元素未访问，则全部剪枝
            if i > 0 and nums[i] == nums[i - 1] and check[i - 1] == 0:
                continue
            check[i] = 1
            self.backTracking(nums, check, path + [nums[i]])
            check[i] = 0
