'''
@Time    : 2020/2/16 15:33
@FileName: 31nextPermutation.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


# 主要是读懂题意，其实排列就是数学中的排列组合，只是参与排列的元素是一个个整数，
# 而这些整数从高位到底为组合起来就是一个多位数的整数，所谓下一个更大的排列
# 即为比这个多位整数大一点数。例如：输入序列为 1,2,3 即组合起来的多位整数为123，
# 而比这个多位整数大一点的整数为132，其元素排列为1,3,2；
#
# 思路：
# 从数组末尾开始，先找到第一个不在正确序列中的数字，即，后一个元素大于前一个元素，记录位置 pos;
# 在 num[pos:] 中找出最小的那个元素(该元素是大于num[pos]中的最小的那个)，记录下标 minPos；
# 交换 num[pos] num[minPos];

class Solution(object):
    def nextPermutation(self, nums):
        if nums is None or len(nums) <= 1:
            return
        pos = None
        p = len(nums) - 1
        # find the first number that is not in correct order
        while p >= 0:
            if nums[p] > nums[p - 1]:
                pos = p - 1
                break
            p -= 1
        print("p:", pos)
        if pos is None:
            self.reverse(nums, 0, len(nums) - 1)
            return
        # find the min value in the rest of the array
        minPos, minV = pos + 1, nums[pos + 1]
        for i in range(pos + 1, len(nums)):
            if nums[i] <= minV and nums[i] > nums[pos]:
                minV = nums[i]
                minPos = i
        print(nums)
        print("pos,minPos", pos, minPos)
        # swap the two above number and reverse the array from `pos`
        nums[pos], nums[minPos] = nums[minPos], nums[pos]
        self.reverse(nums, pos + 1, len(nums) - 1)
        print(nums)
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


if __name__ == '__main__':
    print(Solution().nextPermutation([1,2,3,4,9,8,7]))
