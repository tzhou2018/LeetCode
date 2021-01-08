"""
@Time    : 2020/8/8 21:17
@FileName: 08-08test02.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""


class Solution:
    def nextNum(self, nums):
        pos = None
        p = len(nums) - 1
        while p > 0:
            if nums[p] < nums[p - 1]:
                pos = p - 1
                break
            p -= 1
        if not pos:
            return 0
        maxPos, maxValue = pos + 1, nums[pos + 1]
        for i in range(pos + 1, len(nums)):
            if nums[i] >= maxValue and nums[i] < nums[pos]:
                maxPos = i
                maxValue = nums[i]
        nums[pos], nums[maxPos] = nums[maxPos], nums[pos]
        self.reverseRestNum(nums, pos + 1, len(nums) - 1)
        return int("".join(nums))

    def reverseRestNum(self, nums, start, end):
        while start <= end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def splitNum(self, n):
        res = []
        while n > 0:
            res.append(str(n % 10))
            n //= 10

        return res[::-1]


if __name__ == '__main__':
    solution = Solution()
    n = int(input())
    arrNums = solution.splitNum(n)
    res = Solution().nextNum(arrNums)
    print(res)
