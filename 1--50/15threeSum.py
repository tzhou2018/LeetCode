'''
@Time    : 2020/2/12 20:25
@FileName: 15threeSum.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """
        题目需要我们找出三个数且和为 0 ，那么除了三个数全是 0 的情况之外，
        肯定会有负数和正数，所以一开始可以先选择一个数，然后再去找另外两个数，
        这样只要找到两个数且和为第一个选择的数的相反数就行了。
        也就是说需要枚举 a 和 b ，将 c 的存入 map 即可。
    
        需要注意的是返回的结果中，不能有有重复的结果。
        这样的代码时间复杂度是 O(n^2)。在这里可以先将原数组进行排序，然后再遍历排序后的数组，
        这样就可以使用双指针以线性时间复杂度来遍历所有满足题意的两个数组合。
        """
        res = []
        nums.sort()
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = 0 - nums[i]
            start, end = i + 1, len(nums) - 1
            while start < end:
                if nums[start] + nums[end] > target:
                    end -= 1
                elif nums[start] + nums[end] < target:
                    start += 1
                else:
                    res.append((nums[i], nums[start], nums[end]))
                    end -= 1
                    start += 1
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
        return res


if __name__ == '__main__':
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
