'''
@Time    : 2020/3/28 20:28
@FileName: 46permute.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    # 回溯思想，书写格式1
    # 遍历nums,每次取当前元素num[i]加到tem中，将剩余元素传递给回溯函数nums,
    # 当nums为空是，满足条件的一个序列完成。
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if not nums:
            return []

        def backtracking(nums, tmp):
            if not nums:
                res.append(tmp)
            for i in range(len(nums)):
                backtracking(nums[:i] + nums[i + 1:], tmp + [nums[i]])

        backtracking(nums, [])
        return res


"""
推荐看这个题解过程，讲的很清楚；
其实用到了递归，我们通过画栈图是很容易理解的。

回溯类题一定要考虑的几个方面
有效结果：当长度为输入长度的时候停止，并保存当前结果
回溯条件：每一层都是全部元素遍历：例如答案为[2,1,3]时，第二个元素也是从1开始
剪枝条件：要用check数组来保存用过的元素，用过的不能再用了，这是回溯里面的一个重要考虑因素

作者：sammy-4
链接：https://leetcode-cn.com/problems/permutations/solution/hot-100-46quan-pai-lie-python3-hui-su-step-by-step/
"""


class Solution2:
    def permute(self, nums):
        self.res = []

        check = [0 for i in range(len(nums))]
        self.backtrack([], nums, check)

        return self.res

    def backtrack(self, sol, nums, check):
        if len(sol) == len(nums):
            self.res.append(sol)
            return

        for i in range(len(nums)):
            if check[i] == 1:
                continue
            check[i] = 1
            self.backtrack(sol + [nums[i]], nums, check)
            check[i] = 0


"""
这个是官方题解，不易懂

这里有一个回溯函数，使用第一个整数的索引作为参数 backtrack(first)。

如果第一个整数有索引 n，意味着当前排列已完成。
遍历索引 first 到索引 n - 1 的所有整数。Iterate over the integers from index first to index n - 1.
在排列中放置第 i 个整数，
即 swap(nums[first], nums[i]).
继续生成从第 i 个整数开始的所有排列: backtrack(first + 1).
现在回溯，即通过 swap(nums[first], nums[i]) 还原.


作者：LeetCode
链接：https://leetcode-cn.com/problems/permutations/solution/quan-pai-lie-by-leetcode/
"""


class Solution1:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(first=0):
            # if all integers are used up
            if first == n:
                output.append(nums[:])
            for i in range(first, n):
                # place i-th integer first
                # in the current permutation
                nums[first], nums[i] = nums[i], nums[first]
                # use next integers to complete the permutations
                backtrack(first + 1)
                # backtrack
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        output = []
        backtrack()
        return output
