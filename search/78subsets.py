'''
@Time    : 2020/4/1 22:06
@FileName: 78subsets.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


# 方法1：
# 递归思想，开始输出子集为空，每一步都向子集添加新的整数，并生成新的子集
class Solution:
    def subsets(self, nums):
        n = len(nums)
        output = [[]]

        for num in nums:
            output += [curr + [num] for curr in output]

        return output

# 方法2
# 回溯
# 官方题解：https://leetcode-cn.com/problems/subsets/solution/zi-ji-by-leetcode/
class Solution1:
    def subsets(self, nums):
        output = []
        numsLen = len(nums)

        def backTracking(first=0, curr=[]):
            # recursion terminate
            if len(curr) == k:
                output.append(curr)
            # precess logic in current level
            # drill down
            for i in range(first, numsLen):
                # curr.append(nums[i])
                backTracking(i + 1, curr + [nums[i]])
                # curr.pop()

        for k in range(numsLen + 1):
            backTracking()
        return output


if __name__ == '__main__':
    print(Solution1().subsets([1, 2, 3]))
