'''
@Time    : 2020/2/13 20:53
@FileName: 18fourSum.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


# 同第十五题，求三个数的和。本题使用两层循环，外层循环确定一个数，
# 内层循环可以当做求三个数之和来考虑。
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not nums or len(nums) < 4:
            return []
        nums.sort()
        res = []
        if nums[0] + nums[1] + nums[2] + nums[3] > target:
            return []
        if nums[-1] + nums[-2] + nums[-3] + nums[-4] < target:
            return []
        for i in range(len(nums) - 2):
            if nums[i] + nums[-1] + nums[-2] + nums[-3] < target:
                continue
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] + nums[-2] + nums[-1] < target:
                    continue
                x = j + 1
                y = len(nums) - 1
                while x < y:
                    if nums[i] + nums[j] + nums[x] + nums[y] > target:
                        y -= 1
                    elif nums[i] + nums[j] + nums[x] + nums[y] < target:
                        x += 1
                    else:
                        res.append([nums[i], nums[j], nums[x], nums[y]])
                        x += 1
                        while x < y and nums[x] == nums[x - 1]:
                            x = x + 1

        result = []
        for l in res:
            if l not in result:
                result.append(l)
        return result
# 方法2
"""
把N4拆成2个N2。第一个for循环，先求后2个值可能的取值的所有情况，
并且把它们储存在一个字典里，以和作为键。

第二个for，我们遍历前2个值所可能取的各种值，算出和并且检查target - onesum是否在我们的字典里，
如果在，就说明我们找到了一个解。其实这种求几数之和的问题，
都可以通过这种思路。比如说三数之和，现在我就想到根本不必用指针，
算出所有后2个值所加的可能的和，然后用字典存
最后用target-第一个值去检查是否存在这样的键。

原文链接：https://blog.csdn.net/weixin_40449300/article/details/82467298
"""

class Solution1:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        lens = len(nums)
        dic = {}
        # 先排序后用集合去重
        res = set()
        nums.sort()
        # 先计算前两个数的和
        for i in range(lens - 1):
            for p in range(i + 1, lens):
                key = nums[i] + nums[p]

                if key not in dic:
                    dic[key] = [(i, p)]
                else:
                    dic[key].append((i, p))

        for i in range(2, lens - 1):
            for p in range(i + 1, lens):
                pre = target - nums[i] - nums[p]
                if pre in dic:
                    for index in dic[pre]:
                        # 通过下标判断为合格的后两位数
                        if index[1] < i:
                            res.add((nums[index[0]], nums[index[1]], nums[i], nums[p]))
        return [list(i) for i in res]


if __name__ == '__main__':
    print(Solution1().fourSum([1, 0, -1, 0, -2, 2], 0))
