'''
@Time    : 2020/4/2 10:29
@FileName: 90subsetsWithDup.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backTracking(first=0, curr=[]):
            # recursion terminate
            if len(curr) == k:
                output.append(curr)
                return
            # precess logic in the current level
            # drill down
            for i in range(first, numsLen):
                # 注意这里的剪枝条件，其中 i > start是为了让 nums[i - 1] 在循环中一直有意义。
                if i > first and nums[i] == nums[i - 1]:
                    continue
                backTracking(i + 1, curr + [nums[i]])
                # reverse the level if needed

        numsLen = len(nums)
        output = []
        nums.sort()
        for k in range(numsLen + 1):
            backTracking()
        return output

    # 优化上述解法
    def subsetsWithDup1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backTracking(first=0, curr=[]):
            # recursion terminate
            output.append(curr[:])
            # precess logic in the current level
            # drill down
            for i in range(first, numsLen):
                # 注意这里的剪枝条件，其中 i > start是为了让 nums[i - 1] 在循环中一直有意义。
                if i > first and nums[i] == nums[i - 1]:
                    continue
                backTracking(i + 1, curr + [nums[i]])
                # reverse the level if needed

        numsLen = len(nums)
        output = []
        nums.sort()
        backTracking()
        return output


if __name__ == '__main__':
    print(Solution().subsetsWithDup1([1, 1, 3]))
